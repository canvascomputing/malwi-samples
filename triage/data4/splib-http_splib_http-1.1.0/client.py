import hashlib
import json

import google.protobuf.message
from . import requests_unixsocket
import time
from common import pbutils
from common.logger import log

from . import constant

# Buffer time to be added to the Spex RPC timeout. This is to account for the time
# taken for sending the request to Spex HTTP Gateway and receiving the response.
# Otherwise, the HTTP timeout (Spex RPC timeout + buffer time) will occur, and the
# underlying connection pool drops the connection, which can cause performance issues.
DEFAULT_HTTP_TIMEOUT_BUFFER = 10
MIN_HTTP_TIMEOUT_BUFFER = 1

SR_ID_MAX = 65535
SP_RPC_PATH = "/sprpc/"

CONTENT_TYPE_PROTOBUF = "application/protobuf"
CONTENT_TYPE_JSON = "application/json"

def log_data_request(command, request_id, start_time, request_params, response_body_dict, error, error_msg, log_fields=None, content_type=None):
	#type:(...)->None
	time_elapsed = (time.time() - start_time) * 1000.0
	log.data(
		'splib_rpc_request|id=%s,command=%s,content_type=%s,error=%s,error_msg=%s,time_elapsed=%.3fms,log_fields=%s,params=%s,reply=%s',
		request_id,
		command,
		content_type,
		error,
		error_msg,
		time_elapsed,
		log_fields,
		str(request_params)[:100],
		str(response_body_dict)[:100]
	)

def log_error_request(command, request_id, start_time, request_params, response_content, error, error_msg, log_fields=None, content_type=None):
	#type:(...)->None
	time_elapsed = (time.time() - start_time) * 1000.0
	log.error(
		'splib_rpc_request|id=%s,command=%s,content_type=%s,error=%s,error_msg=%s,time_elapsed=%.3fms,log_fields=%s,params=%s,reply=%s',
		request_id,
		command,
		content_type,
		error,
		error_msg,
		time_elapsed,
		log_fields,
		str(request_params)[:150],
		str(response_content)[:150]
	)

def hash_instance_id(instance_id):
	return hashlib.md5(instance_id.encode()).digest()[-4:]

def get_timestamp_us():
	return int(time.time() * 1000000)

class SpexHTTPAgent(object):

	def __init__(self, instance_id, service_key, request_timeout=None, log_enabled=False, spex_address=None):
		"""

		:param instance_id: instance's id
		:type instance_id: constant.InstanceId or str
		:param service_key: service key
		:type service_key: str
		:param request_timeout: default request timeout,unit: seconds
		:type request_timeout: float
		"""
		self._config = {
			'instance_id': "",
			'instance_id_hash': "",
			'service_key': service_key,
			'request_timeout': request_timeout,
			'log_enabled': log_enabled,
			'url': ''
		}
		if spex_address is None:
			spex_address = "http+unix://%s" % (constant.DEFAULT_SPEX_ADDRESS.replace("/", "%2F"))
		self._config['url'] = "%s%s" % (spex_address, SP_RPC_PATH)
		self._client = requests_unixsocket.Session()
		if isinstance(instance_id, constant.InstanceId):
			self._config["instance_id"] = instance_id.instance_id
			if instance_id.unique_id is None:
				self._client.headers['x-sp-sdu'] = self._config['instance_id']
			else:
				self._client.headers['x-sp-instanceid'] = self._config['instance_id']
		else:
			self._config["instance_id"] = instance_id
		self._config['instance_id_hash'] = hash_instance_id(self._config['instance_id'])
		if request_timeout is None:
			self._config['request_timeout'] = constant.DEFAULT_RPC_REQUEST_TIMEOUT
		self._client.headers['x-sp-servicekey'] = self._config['service_key']
		self._client.headers['Content-type'] = "application/protobuf"

	def request(
			self,
			command,
			request_params,
			request_schema,
			response_schema,
			log_fields=None,
			content_type=CONTENT_TYPE_PROTOBUF,
			**kwargs
	):
		"""
		:type command: str
		:type request_params: dict
		:type request_schema: google.protobuf.message.Message
		:type response_schema: google.protobuf.message.Message
		:type log_fields: any
		:type content_type: str

		:param timeout: (optional) Timeout for the Spex RPC request. Unit: seconds.
		:type timeout: float
		:param http_timeout_buffer: (optional) Additional buffer time to wait for the
			http server to send response before giving up. Note that setting this to a
			value that is too small may cause performance issues. Unit: seconds.
		:type http_timeout_buffer: float

		:rtype: (int, dict)
		"""
		start_time = time.time()
		if content_type == CONTENT_TYPE_PROTOBUF:
			if isinstance(request_params, google.protobuf.message.Message):
				reqbody = request_params.SerializeToString()
			else:
				pb = pbutils.set_pb_from_dict(request_schema(), request_params)
				reqbody = pb.SerializeToString()
		elif content_type == CONTENT_TYPE_JSON:
			if isinstance(request_params, (str, bytes)):
				reqbody = request_params
			else:
				reqbody = json.dumps(request_params)
		else:
			# unknown body type
			reqbody = request_params

		spex_rpc_timeout = kwargs.get('timeout')
		if spex_rpc_timeout is None:
			spex_rpc_timeout = self._config['request_timeout']

		http_timeout_buffer = kwargs.get('http_timeout_buffer')
		if http_timeout_buffer is None:
			http_timeout_buffer = DEFAULT_HTTP_TIMEOUT_BUFFER
		elif http_timeout_buffer < MIN_HTTP_TIMEOUT_BUFFER:
			http_timeout_buffer = MIN_HTTP_TIMEOUT_BUFFER

		http_resp = self._client.post(
			url="%s%s" % (self._config['url'], command),
			timeout=spex_rpc_timeout + http_timeout_buffer,  # Spex already handles timeout via the `x-sp-timeout` header
			data=reqbody,
			headers={
				"x-sp-timeout": str(int(spex_rpc_timeout * 1000)),
				"Content-Type": content_type,
			},
		)

		code = int(http_resp.headers['x-sp-error'])
		err_msg = http_resp.headers['x-sp-errmsg']
		request_id = http_resp.headers.get('x-sp-requestid')
		response_content = http_resp.content

		try:
			if content_type == CONTENT_TYPE_PROTOBUF:
				response_pb = response_schema()
				response_pb.ParseFromString(response_content)
				response_dict = pbutils.pb_to_dict(response_pb, raw=True) if response_pb else {}
			elif content_type == CONTENT_TYPE_JSON:
				response_dict = json.loads(response_content) if response_content else {}
			else:
				# unknown body type
				response_dict = response_content
		except Exception as e:
			log_error_request(command, request_id, start_time, request_params, response_content, e, "splib_http_response_body_exception", log_fields, content_type)
			return constant.ErrorCode.ERROR_SP_BODY, None

		if self._config['log_enabled']:
			log_data_request(command, request_id, start_time, request_params, response_dict, code, err_msg, log_fields, content_type)
		return code, response_dict

	def request_json(
			self,
			command,  #type:str
			request_params,  #type:dict
			log_fields=None,
			**kwargs
	):
		return self.request(
			command=command,
			request_params=request_params,
			request_schema=None,
			response_schema=None,
			log_fields=log_fields,
			content_type=CONTENT_TYPE_JSON,
			**kwargs
		)
