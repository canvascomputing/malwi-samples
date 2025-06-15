import time

import os
import threading
import tornado.ioloop
from tornado import gen
from common import gudsasyncclient
from common import pbutils, jsonutils
from common.logger import log
from sp_protocol.python import common_pb2, spex_pb2

from python_tracing.tracing.span_context import SpanContextGenerator
from python_tracing.tracing.local_context import get_span_context_from_local

from . import locks
from . import spex_request
from . import utils
from . import spcontext
from . import constant


class SpexRequestContext(object):
	__slots__ = ('recv_time', 'header', 'request_id')

	def __init__(self, recv_time, header, request_id):
		self.recv_time = recv_time
		self.header = header
		self.request_id = request_id


class SyncRequestData(object):
	__slots__ = ('event', 'response_header', 'response_body_bytes', 'response_schema')

	def __init__(self):
		self.event = locks.Event()
		self.response_header = None
		self.response_body_bytes = None
		self.response_schema = None


class PassBackData(object):
	__slots__ = ('packet_sended', 'request_id', 'received_from_spex', 'command',)

	def __init__(self):
		self.packet_sended = False
		self.request_id = ''
		self.received_from_spex = False
		self.command = ''


def log_data_request(request_header, request_params, response_header, response_body_dict, error=None, log_fields=None, log_config=None):
	# type: (...) -> None
	if not log_config:
		return
	if not log_config['enable_data_log']:
		return
	log_body_length = log_config['log_body_length']
	if response_header:
		error = response_header.error
	time_elapsed = time.time() * 1000.0 - request_header.timestamp / 1000.0
	if error is None:
		error = constant.ErrorCode.ERROR_SP_INTERNAL
	error_msg = utils.get_error_code_msg(error)
	log.data(
		'splib_rpc_request|id=%s,command=%s,error=%s,error_msg=%s,time_elapsed=%.3fms,log_fields=%s,params=%s,reply=%s',
		spex_request.request_id_to_text(request_header.id),
		request_header.command,
		error,
		error_msg,
		time_elapsed,
		log_fields,
		str(request_params)[:log_body_length],
		str(response_body_dict)[:log_body_length]
	)


class SpexConnection(object):
	"""
	Spex connection
	start must call by creator
	"""

	def __init__(self, service, config, address=None, ident=None):
		# pylint:disable=too-many-arguments
		if address is None:
			address = os.getenv("SP_UNIX_SOCKET")
			if not address:
				address = constant.DEFAULT_SPEX_ADDRESS
		self.config = config
		self.span_context_generator = SpanContextGenerator(self.config.service_instance_info['service_instance_id'])
		self.service = service
		self._state = constant.SpexConnectionStates.NOT_STARTED
		self._established_event = locks.Event()
		self._ioloop = None  # new ioloop for unique connection
		self._ioloop_init_lock = threading.Event()
		self._is_wait_keepalive_response = False
		self._keep_alive_timer = None  # type:tornado.ioloop.PeriodicCallback
		self._address = address
		self._eventdata_map = {}  # type:dict['request_id',SyncRequestData]
		self._conn = None  # type:gudsasyncclient.GUdsAsyncClient
		self._worker_pool = None
		self.need_register_routing = False
		self.need_subscribe_config = False
		self.routing_registered = False
		self.config_subscribed = False
		self._id = ident or threading.current_thread().ident

	@property
	def instance_id(self):
		return self.config.service_instance_info['service_instance_id']

	@property
	def instance_id_hash(self):
		return self.config.service_instance_info['service_instance_id_hash']

	@property
	def instance_tag(self):
		return self.config.service_instance_info['instance_tag']

	@property
	def config_key(self):
		return self.config.service_instance_info['config_key']

	def spawn_worker_pool(self):
		worker_type = self.config.server_config['worker_type']
		pool_size = self.config.server_config['worker_pool_size']
		if worker_type == 'gevent':
			import common.gevent_pool
			self._worker_pool = common.gevent_pool.GeventPool(pool_size)
		elif worker_type == 'thread':
			import common.thread_pool
			self._worker_pool = common.thread_pool.ThreadPool(pool_size)
		else:
			log.exception("splib_worker_type_error|worker_type=%s", worker_type)
			return
		log.info("splib_spwaned_worker_pool|pool_type=%s,pool_size=%s", worker_type, pool_size)

	@property
	def state(self):
		# type:()-> constant.SpexConnectionStates
		return self._state

	@state.setter
	def state(self, new_state):
		if new_state == constant.SpexConnectionStates.ESTABLISHED:
			self._established_event.set()
		else:
			self._established_event.clear()
		log.info("splib_spex_connection_state_change|old_state=%s,new_state=%s", self._state, new_state)
		self._state = new_state

	@gen.coroutine
	def wait_until_established(self, timeout=None):
		"""
		Return True if connection is established
		:param timeout: num of second
		:rtype: bool
		"""
		if timeout is None:
			timeout = 10
		try:
			if not self._established_event.is_set():
				yield self._established_event.wait(timeout=utils.time_after_seconds(timeout))
			resp = self._established_event.is_set()
		except gen.TimeoutError:
			raise gen.Return(False)
		raise gen.Return(resp)

	@gen.coroutine
	def send_request(self, packet_header, packet_body, timeout=None):
		if self.config.log_config['enable_data_log']:
			log.debug(
				'splib_send_packet|command=%s,flag=%s,request_id=%s',
				packet_header.command, packet_header.flag, spex_request.request_id_to_text(packet_header.id))
		packet = spex_request.pack_packet(packet_header, packet_body)
		if len(packet) > constant.DEFAULT_MAX_PACKET_SIZE:
			if packet_header.flag & constant.SpexHeaderFlag.RPC_REPLY:
				# immediately response requester to aviod it wait unnecessary time.
				packet_header.error = constant.ErrorCode.ERROR_SP_BODY
				packet = spex_request.pack_packet(packet_header, None)
			else:
				raise gen.Return(constant.ErrorCode.ERROR_EXCEED_LIMIT)
		#  if we send request after timeout, client is go away.
		if packet_header.command not in {constant.SpexCommand.SUBSCRIBE_CONFIG, constant.SpexCommand.REGISTER_ROUTING}:
			wait_start_time = self._ioloop.time()
			established = yield self.wait_until_established(timeout=timeout)
			wait_elapsed_time = self._ioloop.time() - wait_start_time
			if not established:
				log.warning(
					"splib_send_request_packet_but_connection_established_too_late|request_id=%s,wait_elapsed_time=%ss",
					spex_request.request_id_to_text(packet_header.id), wait_elapsed_time)
				#  no need to send the packet
				return
		self._conn.send(packet)

	def request(self, *args, **kwargs):
		ctx = spcontext.get_context()
		# Makesure if call from other thread (no ioloop thread) will dispatch to ioloop thread call this callback
		# block other thread unitl reply arrived
		ctx["span_context"] = get_span_context_from_local()

		pass_back_data = PassBackData()
		error_code, resp = utils.call_coroutine(
			self.co_request,
			*args,
			context=ctx,
			timeout_result=(constant.ErrorCode.ERROR_SP_TIMEOUT, None),
			ioloop=self._ioloop,
			pass_back_data=pass_back_data,
			**kwargs
		)

		if error_code != constant.ErrorCode.SUCCESS:
			log.error(
				"splib_rpc_request_reply_error|request_id=%s,command=%s,packet_sended=%s,is_received_from_spex=%s,error_code=%s,error_msg=%s",
				pass_back_data.request_id,
				pass_back_data.command,
				pass_back_data.packet_sended,
				pass_back_data.received_from_spex,
				error_code,
				utils.get_error_code_msg(error_code),
			)
		return error_code, resp

	def async_request(self, command, request_params, request_schema, response_schema, timeout=None, callback=None):
		ctx = spcontext.get_context()

		@gen.coroutine
		def cb():
			code, resp = yield self.co_request(
				command, request_params, request_schema=request_schema,
				response_schema=response_schema, timeout=timeout, context=ctx)
			self.add_task_to_worker_pool(callback, code, resp)

		self._ioloop.add_callback(cb)

	@gen.coroutine
	def co_request(  # pylint:disable=too-many-arguments
		self, command, request_params, request_schema, response_schema, as_dict=True,
		timeout=None, context=None,
		log_fields=None,
		pass_back_data=None  # type: PassBackData
	):
		"""
		sync rpc request,but base on eventloop
		"""
		if not self.routing_registered and command not in constant.ALLOW_NOTREGISTER_COMMAND:
			raise gen.Return((constant.ErrorCode.ERROR_SP_NOT_INIT, None))

		request_id = None
		response_header = None
		response_body = None

		try:
			request_header, request_data = spex_request.get_request_data(
				command, request_params, request_schema=request_schema, instance_id=self.instance_id,
				span_context_generator=self.span_context_generator, context=context, timeout=timeout)
		except Exception:
			log.exception('splib_get_request_data_error')
			raise gen.Return((constant.ErrorCode.ERROR_SP_PARAMS, None))
		if pass_back_data is not None:
			pass_back_data.request_id = spex_request.request_id_to_text(request_header.id)
			pass_back_data.command = command
		event_data = SyncRequestData()
		self._eventdata_map[request_header.id] = event_data
		#  async send request packet
		send_code = yield self.send_request(request_header, request_data, timeout=timeout)
		if send_code == constant.ErrorCode.ERROR_EXCEED_LIMIT:
			self._eventdata_map.pop(request_header.id)
			raise gen.Return((constant.ErrorCode.ERROR_EXCEED_LIMIT, None))
		if pass_back_data is not None:
			pass_back_data.packet_sended = True
		if timeout is None:
			ev_timeout = constant.DEFAULT_REQUEST_TIMEOUT + 5
		else:
			ev_timeout = timeout + 5
		if not event_data.event.is_set():
			try:
				log.debug("splib_ioloop_wait|timeout=%s", ev_timeout)
				yield event_data.event.wait(timeout=utils.time_after_seconds(ev_timeout))
			except tornado.gen.TimeoutError:
				log.warning("splib_request_timout|request_id=%s,command=%s", spex_request.request_id_to_text(request_header.id), command)
				log_data_request(
					request_header, request_params, None, None, error=constant.ErrorCode.ERROR_SP_TIMEOUT, log_fields=log_fields,
					log_config=self.config.log_config)
				raise gen.Return((constant.ErrorCode.ERROR_SP_TIMEOUT, None))
			finally:
				if self._eventdata_map.pop(request_header.id, None) is None:
					log.warning("splib_already_pop_event_data|request_id=%s", request_header.id)
		try:
			if pass_back_data is not None:
				pass_back_data.received_from_spex = True
			response_header, response_body_bytes = event_data.response_header, event_data.response_body_bytes
			request_id = spex_request.RequestId(response_header.id)
			if not response_header.flag & constant.SpexHeaderFlag.RPC_REPLY:
				log.error('splib_response_header_flag_error|id=%s,command=%s,flag=%s', request_id, command, response_header.flag)
				raise gen.Return((constant.ErrorCode.ERROR_SP_HEADER, response_body))
			if request_header.source and response_header.key != '@.' + request_header.source:
				log.error('splib_response_header_key_error|key=%s,source=%s', response_header.key, request_header.source)
				raise gen.Return((constant.ErrorCode.ERROR_SP_HEADER, response_body))
			response_body = spex_request.parse_body(response_body_bytes, response_schema)
			response_body_dict = pbutils.pb_to_dict(response_body, raw=True)

			log_data_request(request_header, request_params, response_header, response_body_dict, log_fields=log_fields, log_config=self.config.log_config)
			if as_dict:
				raise gen.Return((response_header.error, response_body_dict))
			else:
				raise gen.Return((response_header.error, response_body))

		except gen.Return:
			raise
		except Exception:
			log.exception(
				'splib_rpc_request_fail|id=%s,command=%s,params=%s,error=%s,reply=%s',
				request_id, request_header.command,
				str(request_data), response_header.error, str(response_body))
			log_data_request(request_header, request_params, response_header, None, log_fields=log_fields, log_config=self.config.log_config)
			raise gen.Return((constant.ErrorCode.ERROR_SP_INTERNAL, response_body))

	def _send_keepalive(self):
		if self._is_wait_keepalive_response:
			log.warn('splib_spconnection_waiting_keepalive_reply_timeout|id=%s', self._conn.id)
			self.reconnect()
			self._is_wait_keepalive_response = False
			return
		self._is_wait_keepalive_response = True
		request_header, request_body = spex_request.get_request_data(
			constant.SpexCommand.KEEP_ALIVE, {}, request_schema=common_pb2.KeepAliveRequest, 
			instance_id=self.instance_id,span_context_generator=self.span_context_generator)
		self.send_request(request_header, request_body)

	def _setup_keepalive(self):
		self._keep_alive_timer = tornado.ioloop.PeriodicCallback(callback=self._send_keepalive, callback_time=10 * 1000)
		self._keep_alive_timer.start()

	def _on_receive_packet(self, _conn, packet):
		try:
			packet_header_bytes, packet_body_bytes = spex_request.unpack_packet_raw(packet)
			packet_header = spex_request.parse_header(packet_header_bytes)
		except Exception as e:
			log.exception('splib_spex_connection_unpack_packet_exception|packet=%s,exc=%r', packet.encode('hex'), e)
			self.reconnect()
			return
		request_id = spex_request.RequestId(packet_header.id)
		if self.config.log_config['enable_data_log']:
			log.debug("splib_receive_packet|id=%s,command=%s,flag=%s", request_id, packet_header.command, packet_header.flag)
		# packet is keepalive response
		if packet_header.command == constant.SpexCommand.KEEP_ALIVE and packet_header.flag & constant.SpexHeaderFlag.RPC_REPLY:
			log.debug('splib_spconnection_config_worker_keepalive_responsed')
			self._is_wait_keepalive_response = False
			return
		# Request packet block
		if not packet_header.flag & constant.SpexHeaderFlag.RPC_REPLY:
			# TRICKY: If SubscribeConfig is not completed, drop all other packets.
			if self.state != constant.SpexConnectionStates.ESTABLISHED:
				log.warning("splib_drop_request_packet_on_connecting")
				return
			if packet_header.command == constant.SpexCommand.NOTIFY_CONFIG_UPDATE:
				try:
					notify_config_update_request = spex_request.parse_body(packet_body_bytes, spex_pb2.NotifyConfigUpdateRequest)
					for config in notify_config_update_request.configs:
						self.config.update_config(key=config.key, data=jsonutils.from_json_safe(config.value), version=notify_config_update_request.version)
				except Exception:
					log.exception("splib_notify_config_update_exception")
				# Reply to spex
				reply_header = spex_request.get_reply_header(packet_header, instance_id=self.instance_id)
				reply = spex_pb2.NotifyConfigUpdateResponse()
				reply_data = reply.SerializeToString()
				self.send_request(reply_header, reply_data)
				return
			# request packet
			self.on_receive_request_packet(packet_header=packet_header, packet_body_bytes=packet_body_bytes)
		# Response packet block
		elif packet_header.id in self._eventdata_map:
			# awake sync request coroutine
			event_data = self._eventdata_map[packet_header.id]
			event_data.response_header = packet_header
			event_data.response_body_bytes = packet_body_bytes
			event_data.event.set()
		else:
			log.warning(
				"splib_drop_unknow_packet|id=%s,command=%s,flag=%s", request_id, packet_header.command,
				packet_header.flag)

	@gen.coroutine
	def _on_disconnect(self, _conn):
		if self._keep_alive_timer is not None:
			self._keep_alive_timer.stop()
		# Reset flags
		self.state = constant.SpexConnectionStates.CONNECTING
		self.routing_registered = False
		self.config_subscribed = False

	@gen.coroutine
	def _on_connect(self, client):
		self._setup_keepalive()
		self.state = constant.SpexConnectionStates.SUBSCRIBING_CONFIG
		ok = yield self.subscribe_config_if_needed()
		if not ok:
			self.reconnect()
			return
		self.state = constant.SpexConnectionStates.REGISTERING_ROUTING
		ok = yield self.register_routing_if_needed()
		if not ok:
			self.reconnect()
			return
		self.state = constant.SpexConnectionStates.ESTABLISHED
		log.info("splib_spex_connection_connected|instance_id=%s", self.instance_id)

	def reconnect(self):
		self.config_subscribed = False
		self.routing_registered = False
		self._ioloop.call_later(constant.RECONNECT_DELAY, self._conn.reconnect)

	def _ensure_connection(self):
		self._conn = gudsasyncclient.GUdsAsyncClient(
			id='',
			address=self._address,
			port=None,
			on_receive_packet=self._on_receive_packet,
			on_disconnect=self._on_disconnect,
			on_connect=self._on_connect,
			max_packet_size=constant.DEFAULT_MAX_PACKET_SIZE
		)
		self.spawn_worker_pool()

	def create_new_ioloop(self):
		self._ioloop = tornado.ioloop.IOLoop()
		return self._ioloop

	def ioloop(self):
		if not self._ioloop_init_lock.isSet():
			self._ioloop_init_lock.wait()
		return self._ioloop

	def run(self):
		self._ioloop = tornado.ioloop.IOLoop()
		self._ioloop.make_current()
		self._ioloop_init_lock.set()

		self._ioloop.add_callback(self._ensure_connection)
		self._ioloop.start()

	@property
	def name(self):
		return '<%s-%s>' % (self.__class__.__name__.lower(), threading.currentThread().ident)

	@gen.coroutine
	def register_routing_if_needed(self):
		if self.need_register_routing and not self.routing_registered:
			resp = yield self.register_routing()
			raise gen.Return(resp)
		raise gen.Return(True)

	@gen.coroutine
	def subscribe_config_if_needed(self):
		if self.need_subscribe_config and not self.config_subscribed:
			resp = yield self.subscribe_config()
			raise gen.Return(resp)
		raise gen.Return(True)

	@gen.coroutine
	def register_routing(self):
		log.info('splib_spconnection_register_routing')
		try:
			self.config.sp_service_info
		except (KeyError, AttributeError) as e:
			log.warning("splib_register_routing_sp_service_info_not_configured|err=%r", e)
			raise gen.Return(False)

		register_params = {
			'instance_id': self.instance_id,
			'service_name': self.config.sp_service_info['service_name'],
			'service_key': self.config.sp_service_info['service_key'],
			'routing_rules': self.config.routing_info['routing_rules'],
		}
		log.info("splib_spex_connection_register_routing")
		error_code, _ = yield self.co_request(
			command=constant.SpexCommand.REGISTER_ROUTING,
			request_params=register_params,
			request_schema=spex_pb2.RegisterRoutingRequest,
			response_schema=spex_pb2.RegisterRoutingResponse,
		)
		if error_code != constant.ErrorCode.SUCCESS:
			raise gen.Return(False)
		log.info('splib_spconnection_routing_registered')
		# Set up endpoint ID
		self.routing_registered = True
		log.info('splib_spconnection_register_routing_success')
		raise gen.Return(True)

	def close_connection(self):
		error_code, _ = self.request(constant.SpexCommand.UNREGISTER_ROUTING, {}, spex_pb2.UnregisterRoutingRequest, spex_pb2.UnregisterRoutingResponse)
		if error_code != constant.ErrorCode.SUCCESS:
			raise Exception('unregister_routing_exception')

	@gen.coroutine
	def subscribe_config(self):
		log.info('splib_spconnection_subscribe_config')
		subscribe_params = {
			'instance_id': self.instance_id,
			'config_key': self.config_key,
		}
		error_code, response = yield self.co_request(
			command=constant.SpexCommand.SUBSCRIBE_CONFIG,
			request_params=subscribe_params,
			request_schema=spex_pb2.SubscribeConfigRequest,
			response_schema=spex_pb2.SubscribeConfigResponse,
			as_dict=False
		)
		log.data('splib_client_worker_subscribe_config_request|params=%s', subscribe_params)

		# Return value from subscribe config command, update config
		# TODO: set read timeout of tcp client to 0
		if error_code != constant.ErrorCode.SUCCESS:
			log.warning('splib_spconnection_mainconn_subscribe_config_fail|error=%s', error_code)
			raise gen.Return(False)
		log.data('splib_spconnection_config_subscribed|config_version=%s', response.version)
		for config in response.configs:
			self.config.update_config(key=config.key, data=jsonutils.from_json_safe(config.value), version=response.version)
		self.config_subscribed = True
		log.info('splib_spconnection_subscribe_config_success')
		raise gen.Return(True)

	def process_packet_and_send_reply(self, request_context, packet_body_bytes):
		"""

		:type packet_body_bytes: str
		:type request_context: SpexRequestContext
		"""
		# TODO: add overload protection logic
		packet_header = request_context.header
		service_info = self.service.get_service(packet_header.command)
		reply_body = constant.ErrorCode.ERROR_SP_INTERNAL
		try:
			if not service_info:
				log.warning(
					'splib_spserver_service_not_found|id=%s,request_id=%s,command=%s',
					self._id, request_context.request_id, packet_header.command)
				reply_body = constant.ErrorCode.ERROR_NOT_IMPLEMENTED
				return
			else:
				try:
					packet_body = spex_request.parse_body(packet_body_bytes, service_info['request_schema'])
				except Exception:
					log.exception(
						'splib_spserver_parse_body_exception|id=%s,packet_body=%s', self._id,
						packet_body_bytes.encode('hex'))
					reply_body = constant.ErrorCode.ERROR_PARAMS
					return
				packet_body_dict = pbutils.pb_to_dict(packet_body, raw=True)
				start_time = time.time()
				wait_elapsed = int((start_time - request_context.recv_time) * 1000)
				try:
					# processor has two arguments  request_context and  packet_body_dict
					with spex_request.server_request_context(packet_header, packet_body, self.instance_id):
						reply_body = service_info['function'](request_context, packet_body_dict)
					log.debug("splib_processor_process|request_body=%s,reply_body=%s", packet_body_dict, reply_body)
				except Exception:
					process_elapsed = int((time.time() - start_time) * 1000)
					log.exception(
						'splib_spserver_process_packet_exception|id=%s,request_id=%s,key=%s,command=%s,source=%s,wait=%s,process=%s,params=%s',
						self._id, request_context.request_id, packet_header.key, packet_header.command,
						packet_header.source, wait_elapsed, process_elapsed, jsonutils.to_json(packet_body_dict))
					reply_body = constant.ErrorCode.ERROR_SP_SERVICE_UNAVAILABLE
					return
				process_elapsed = int((time.time() - start_time) * 1000)
				log.data(
					'splib_spserver_process_packet|id=%s,request_id=%s,key=%s,command=%s,source=%s,wait=%s,process=%s,params=%s,response=%s',
					self._id, request_context.request_id, packet_header.key, packet_header.command,
					packet_header.source, wait_elapsed, process_elapsed, jsonutils.to_json(packet_body_dict),
					jsonutils.to_json(reply_body))
		finally:
			if isinstance(reply_body, dict):
				reply_header = spex_request.get_reply_header(packet_header, instance_id=self.instance_id)
				try:
					reply_body = pbutils.set_pb_from_dict(service_info['response_schema'](), reply_body)
				except Exception:
					log.exception("splib_pack_reply_body_exception|schema=%s,reply_body=%s", service_info['response_schema'], reply_body)
					reply_header.error = constant.ErrorCode.ERROR_SP_BODY
					reply_body = None
			else:
				reply_header = spex_request.get_reply_header(packet_header, instance_id=self.instance_id, error=reply_body)
				reply_body = None
			# TODO (liuyang): if process elapsed more than 60s, is necessary to send reply?
			self._ioloop.add_callback(self.send_request, reply_header, reply_body)

	@gen.coroutine
	def on_receive_request_packet(self, packet_header, packet_body_bytes):
		recv_time = time.time()

		# At this point, self._is_config_subscribed == True
		# TODO: handle spex register routing request timeout
		request_context = SpexRequestContext(recv_time, packet_header, spex_request.RequestId(packet_header.id))
		self.add_task_to_worker_pool(self.process_packet_and_send_reply, request_context, packet_body_bytes)

	def add_task_to_worker_pool(self, func, *args, **kwargs):
		if self._worker_pool is None:
			self.spawn_worker_pool()
		self._worker_pool.add_task(func, args=args, kwargs=kwargs)
