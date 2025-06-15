"""
Spex server interface.
This module is used by microservices to register to receive requests and configuration updates from Spex.

Services are required to implement the methods to process requests that they have registered routing for
(under `routing_info['routing_rules']`) via the `spservice` module.

Required configs in Space:
- sp_service_info
	- service_name: Name of service
	- service_key: Service key for authentication of commands
- routing_info
	- routing_rules list: List of strings for which Spex should route commands to.
	- routing_weight uint: Routing weight
- server_config
	- connection_worker_size int:
	- worker_type string: Type of worker to process requests. Currently support `thread` or `gevent`
	- worker_pool_size int: Number of workers per connection.
	- process_size int: Number of process to serve, also Number of connections the service
						should maintain with Spex. This defines the number of processes as
						each process maintains a connection with Spex.

Usage:

	If your application is a service

	>>> import splib
	>>> splib.init()
	>>> splib.serve()

	Or application is only use splib to request

	>>> import __init__ as splib
	>>> splib.init()
	>>> splib.register()


	Both way connection already started, you can write following code to make request
		>>> response_code, response_dict = splib.rpc_request(
		>>> ...command='python.demo.echo',
		>>> ...request_params={'data':'hello world!'},
		>>> ...request_schema=request_schema,
		>>> ...response_schema=response_schema
		>>> )
		>>>
"""

import os
import threading

from common.logger import log

from . import constant
from . import errors
from . import token_bucket
from . import spconfig
from . import spex_connection
from . import spservice
from . import utils


class Agent(object):
	def __init__(self):
		self.config = spconfig.Config(agent=self)
		self.service = spservice.SpService(self.config)
		self.spex_connection = None  # type:spex_connection.SpexConnection
		self.spex_connection_thread = None
		self.name = None
		self._thread_lock = threading.Lock()
		self.token_bucket = token_bucket.TokenBucket()

	def set_rate_limit(self, rate):
		"""

		:param rate: number of limit per second
		"""
		self.token_bucket.set_rate(rate)

	def async_rpc_request(self, command, request_params, request_schema, response_schema, timeout=None, callback=None):
		"""

		:param command: command string
		:param request_params: request data
		:param request_schema:  protobuf message schema of request
		:param response_schema: protobuf message schema of response
		:param timeout time of seconds, default is DEFAULT_REQUEST_TIMEOUT
		:type command: str
		:type timeout int
		:param callback: callback function defined as
			>>> def callback(error_code,response_body_dict)
		:return:
		"""
		return self.spex_connection.async_request(
			command, request_params, request_schema=request_schema, response_schema=response_schema, timeout=timeout,
			callback=callback)

	def rpc_request(self, command, request_params, request_schema, response_schema, timeout=None, log_fields=None, as_dict=True):
		# type: (...)->(int,dict) | (int,object)
		"""
		Request to Spex synchronously.
		:param command: command string
		:param request_params: request data
		:param request_schema:  protobuf message schema of request
		:param response_schema: protobuf message schema of response
		:param timeout time of seconds, default is DEFAULT_REQUEST_TIMEOUT
		:param log_fields: extra fields need write to log
		:param as_dict: whether to return response as dict or pb
		:type command: str
		:type timeout int
		:type as_dict: bool
		"""
		if not self.is_connected():
			return constant.ErrorCode.ERROR_NOT_INIT, None
		if not self.token_bucket.can_do_once():
			log.error("splib_rpc_request_quota|command=%s,tokens=%s", command, self.token_bucket.tokens)
			return constant.ErrorCode.ERROR_QUOTA_LIMIT, None
		error_code, reply = self.spex_connection.request(
			command=command,
			request_params=request_params,
			request_schema=request_schema,
			response_schema=response_schema,
			timeout=timeout,
			log_fields=log_fields,
			as_dict=as_dict,
		)

		return error_code, reply

	def init(self, instance_id=None, config_key=None, instance_tag=None):
		"""
		:param instance_id: `class InstanceId`'s instance or str or unicode string
		:param instance_tag: string of instance_tag
		:param config_key: string of config_key
		:return:
		"""
		if instance_id is None:
			instance_id = os.getenv('SP_INSTANCE_ID')
		elif isinstance(instance_id, str):
			instance_id = instance_id
		elif isinstance(instance_id, bytes):
			instance_id = instance_id.decode()
		elif isinstance(instance_id, constant.InstanceId):
			instance_id = instance_id.instance_id
		else:
			raise errors.SPException("unknow instance_id")
		if instance_tag is None:
			instance_tag = os.getenv('SP_INSTANCE_TAG', '')
		else:
			instance_tag = instance_tag
		if config_key is None:
			config_key = os.getenv('SP_CONFIG_KEY')
		else:
			config_key = config_key
		instance_id_hash = utils.service_instance_id_hash(instance_id)
		self.config.init_config(service_instance_id=instance_id, config_key=config_key, instance_tag=instance_tag, instance_id_hash=instance_id_hash)
		self.spex_connection = spex_connection.SpexConnection(
			config=self.config, service=self.service)
		utils.try_setup_resolver()
		log.info("splib_init|instance_id=%s,config_key=%s", instance_id, config_key)

	def _wait_established(self, timeout=constant.SPLIB_START_TIMEOUT):
		return utils.call_coroutine(self.spex_connection.wait_until_established, timeout=timeout, ioloop=self.spex_connection.ioloop())

	def _ensure_spex_thread(self):
		if not self.spex_connection_thread:
			self.spex_connection_thread = threading.Thread(target=self._serve, args=(None,))
			self.spex_connection_thread.daemon = True
			self.spex_connection_thread.start()

	def register(self):
		"""
		Register to spex
		:return: True if registered
		"""
		with self._thread_lock:
			if not self.spex_connection.need_subscribe_config:
				# Disallow implicit subscribe config
				raise errors.SPStartError("must subscribe config first")
			self.spex_connection.need_register_routing = True
			if self.spex_connection.routing_registered:
				log.warning("splib_already_register_routing")
				return True
			self._ensure_spex_thread()
			self._wait_established()
			resp = utils.call_coroutine(self.spex_connection.register_routing_if_needed, ioloop=self.spex_connection.ioloop())
			if resp:
				log.info("splib_registered")
			else:
				self.spex_connection.reconnect()
			return resp

	def subscribe_config(self):
		with self._thread_lock:
			if self.spex_connection.config_subscribed:
				log.warning("splib_already_subscribe_config")
				return True
			self.spex_connection.need_subscribe_config = True
			self._ensure_spex_thread()
			established = self._wait_established()
			if not established:
				load_cache_success = self.config._load_cache()  # pylint:disable=protected-access
				if not load_cache_success:
					self.spex_connection.ioloop().stop()
					self.spex_connection_thread = None
					raise errors.SPStartTimeoutAndConfigCacheLoadError("splib_start_error_and_config_cache_load_error")
				log.warning("splib_start_timeout_retry_in_background")
				return False
			log.info('splib_config_subscribed')
			return True

	def _serve(self, name):
		self.name = name
		if not (not name or name == 0):
			# Forked child process must have own ioloop,can't share with parent process
			self.spex_connection.create_new_ioloop()
		try:
			self.spex_connection.run()
		except KeyboardInterrupt:
			import sys
			log.warning("splib_keyboard_interrupt_exiting")
			sys.stderr.flush()
			self.spex_connection.ioloop().add_callback(os._exit(1))  # pylint:disable=protected-access

	def serve(self):
		"""
		This function will run forever
		should call if your program is service
		"""
		process_size = self.config.server_config['process_size']
		self.spex_connection.need_subscribe_config = True
		self.spex_connection.need_register_routing = True
		if process_size == 1:
			self._serve(0)
		else:
			import multiprocessing
			for i in range(process_size):
				p = multiprocessing.Process(target=self._serve, args=('agent-{}'.format(i),))
				p.start()
			os.wait()

	def is_connected(self):
		# type: ()->bool
		with self._thread_lock:
			if not self.spex_connection:
				return False
			return self.spex_connection.routing_registered and self.spex_connection.config_subscribed

	@property
	def state(self):
		# type:()->constant.SpexConnectionStates
		with self._thread_lock:
			if not self.spex_connection:
				return constant.SpexConnectionStates.NOT_STARTED
			return self.spex_connection.state


# The default agent
agent = Agent()

# Module level agent methods
init = agent.init
register = agent.register
serve = agent.serve
config = agent.config
register_config_update_callback = config.register_config_update_callback
register_service = agent.service.register_service
rpc_request = agent.rpc_request
async_rpc_request = agent.async_rpc_request
subscribe_config = agent.subscribe_config
is_connected = agent.is_connected
set_rate_limit = agent.set_rate_limit
