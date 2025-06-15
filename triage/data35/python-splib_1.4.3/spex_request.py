import codecs
import contextlib

from google.protobuf import message

from common import buffer_reader
from common import buffer_writer
from common import pbutils
from common.logger import log
from sp_protocol.python import common_pb2

from .utils import get_timestamp_us
from . import spcontext
from . import constant

SR_LEVEL_MAX = 255
SR_ID_MAX = 65535


class SpexRequest(object):
	def __init__(self, header, body):
		self.header = header
		self.body = body


@contextlib.contextmanager
def server_request_context(packet_header, packet_body, instance_id):
	ctx = spcontext.get_context()
	ctx['current_request'] = SpexRequest(packet_header, packet_body)
	# The value associated to this key is returned by a deprecated function.
	# The previous function returned the old request_id format and we keep it here to not break anything depending on it
	# In case, you are not relying on the old format, please use the new python tracing library instead
	ctx['client_status'] = get_next_level_client_status(packet_header.id, instance_id=instance_id)
	try:
		yield
	finally:
		ctx.pop('current_request')
		ctx.pop('client_status')


def get_next_request_id(span_context_generator, context):
	if context is not None:
		span_context = context["span_context"]
		if span_context:
			return span_context.new_child_span_context().get_bytes()
	return span_context_generator.new_span_context().get_bytes()


def get_next_level_client_status(request_id, instance_id):
	"""
	Retrieve the next level request client status from the request ID.
	"""
	client_status = {}
	client_status['trace_id'] = request_id[:16]
	client_status['parent_span_id'] = request_id[16:24]
	reader = buffer_reader.BufferReader(client_status['parent_span_id'], endian='!')
	client_status['sr_level'] = reader.get_uint8() + 1
	if client_status['sr_level'] > SR_LEVEL_MAX:
		log.warning(
			'splib_[spex]sr_level_overflow|instance_id=%s,trace_id=%s,client_status=%s',
			instance_id, client_status['trace_id'], client_status)
		client_status['sr_level'] = 0
	client_status['sr_id'] = -1
	return client_status


def get_request_data(command, request_params, instance_id, span_context_generator, request_schema, context=None, timeout=None):
	request_header = common_pb2.SpexHeader()
	request_header.id = get_next_request_id(span_context_generator, context)
	request_header.flag = 0  # rpc_request + normal_request
	request_header.key = command
	request_header.command = command
	request_header.qos.priority = constant.DEFAULT_QOS_PRIORITY
	if timeout is None:
		request_header.qos.timeout = int(constant.DEFAULT_REQUEST_TIMEOUT * 1000)
	else:
		if not isinstance(timeout, (int, float)):
			raise ValueError("timeout must int or float got %r" % timeout)
		if not timeout > 0:
			raise ValueError("timeout must > 0 , got %s" % timeout)
		request_header.qos.timeout = int(timeout * 1000)
	request_header.version = 0  # TODO
	request_header.source = instance_id

	if isinstance(request_params, message.Message):
		request_data = request_params
	else:  # transform request dict to protobuf object
		request_data = pbutils.set_pb_from_dict(request_schema(), request_params)

	return request_header, request_data


def get_reply_header(request_header, error=constant.ErrorCode.SUCCESS, instance_id=None, priority=None, version=None):
	reply_header = common_pb2.SpexHeader()
	reply_header.CopyFrom(request_header)
	reply_header.flag |= constant.SpexHeaderFlag.RPC_REPLY
	reply_header.key = constant.SPEX_ROUTING_ENDPOINT_IDENTIFIER + request_header.source
	if priority is not None:
		reply_header.qos.priority = priority
	else:
		reply_header.qos.priority = constant.DEFAULT_QOS_PRIORITY
	reply_header.version = version or 0
	request_header.source = instance_id

	reply_header.error = error
	log.debug("splib_reply header :flag:%d key:%s", reply_header.flag, reply_header.key)

	return reply_header


def request_id_to_text(request_id):
	request_id_hex = codecs.encode(request_id, 'hex')
	return '%s:%s:%s' % (request_id_hex[:32], request_id_hex[32:48], request_id_hex[48:])


class RequestId(object):

	def __init__(self, request_id):
		self._id = request_id
		self._id_text = request_id_to_text(request_id)

	def __str__(self):
		return self._id_text

	@property
	def text(self):
		return self._id_text

	@property
	def bytes(self):
		return self._id


def pack_packet(header, body):
	header.timestamp = get_timestamp_us()

	header_bytes = header.SerializeToString()
	body_bytes = body.SerializeToString() if body else ''

	writer = buffer_writer.BufferWriter(endian='<')
	writer.add_uint16(len(header_bytes))
	writer.add_buffer(header_bytes)
	writer.add_buffer(body_bytes)
	return writer.buffer


def unpack_packet(packet_bytes, body_schema):
	header_bytes, body_bytes = unpack_packet_raw(packet_bytes)

	header = parse_header(header_bytes)
	body = parse_body(body_bytes, body_schema)

	return header, body


def unpack_packet_raw(packet_bytes):
	reader = buffer_reader.BufferReader(packet_bytes, endian='<')
	header_length = reader.get_uint16()
	header_bytes = reader.get_buffer(header_length)
	body_bytes = reader.get_remain()

	if reader.error:
		raise Exception('reply_packet_format_error')

	return header_bytes, body_bytes


def parse_header(header_bytes):
	header = common_pb2.SpexHeader()
	header.ParseFromString(header_bytes)
	return header


def parse_body(body_bytes, body_schema):
	body = body_schema()
	if not body_bytes:
		return body
	body.ParseFromString(body_bytes)
	return body
