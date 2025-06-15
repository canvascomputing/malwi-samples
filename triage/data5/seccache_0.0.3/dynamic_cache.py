import redis
from redis.connection import Connection
import re
from common.cache import _cache_classes, DistributionCache, BaseCache, create_cache_client
from common.conhash import ConHash
from common import conhash


class DynamicRedisConnection(Connection):
	description_format = "DynamicRedisConnection<service_name=%(service_name)s,db=%(db)s>"

	def __init__(self, *args, **kwargs):
		self._service_dependency_manager = kwargs['service_dependency_manager']
		del kwargs['service_dependency_manager']
		self._service_name = kwargs['service_name']
		del kwargs['service_name']

		self.host = None
		self.port = None
		self._addrs = []
		self._update()

		kwargs.update({
			'host': self.host,
			'port': self.port,
		})

		super(DynamicRedisConnection, self).__init__(*args, **kwargs)

	def _update(self):
		addrs = self._service_dependency_manager.get_service_addrs(self._service_name)
		if len(addrs) == 0:
			return

		if addrs == self._addrs:
			return

		self._addrs = addrs

		for addr in self._addrs:
			host, port = addr.split(':')
			port = int(port)

			if self.host != host or self.port != port:
				# from common.logger import log
				# log.debug('dynamic_redis_connection_pool|new_addr=%s:%s,old_addr=%s:%s',
				# 			host, port, self._host, self._port)

				self.host = host
				self.port = port
				return

	def _connect(self):
		self._update()
		return super(DynamicRedisConnection, self)._connect()


# Don't import anything from settings, otherwise would cause cycle dependencies.
class DynamicRedisConnectionPool(redis.BlockingConnectionPool):

	def __init__(self, service_dependency_manager=None, service_name=None, **connection_kwargs):
		if 'db' not in connection_kwargs:
			connection_kwargs['db'] = 0

		if 'connection_class' in connection_kwargs:
			del connection_kwargs['connection_class']

		connection_kwargs.update({
			'service_dependency_manager': service_dependency_manager,
			'service_name': service_name,
		})

		self.connection_kwargs = connection_kwargs

		super(DynamicRedisConnectionPool, self).__init__(
			connection_class=DynamicRedisConnection,
			**self.connection_kwargs)


class DynamicDistributionCache(DistributionCache):

	def __init__(self, config):
		BaseCache.__init__(self, config)
		self._client = {}
		self._id = config['id']
		self._client_config = config['client_config']
		self._service_name = config['service_name']
		self._method = config.get('method')
		self._conhash = self._create_conhash()

		self._service_dependency_manager = config['service_dependency_manager']

		if self._method in ('mod', 'div', 'hash_mod', 'hash_div'):
			self.get_client_by_key = {
				'mod': self._get_client_by_key_mod,
				'div': self._get_client_by_key_div,
				'hash_mod': self._get_client_by_key_hash_mod,
				'hash_div': self._get_client_by_key_hash_div,
			}[self._method]
			self._init = self._init_method_mod_div
			self._update = self._update_method_mod_div
		else:
			self.get_client_by_key = self._get_client_by_key_conhash
			self._init = self._init_method_conhash
			self._update = self._update_method_conhash

		self._init(config)
		self._addrs = []
		self._update()

	def _create_conhash(self):
		hash_method = getattr(conhash, 'HASH_METHOD_MD5', None)
		if getattr(conhash, 'HASH_METHOD_MD5', None) is not None:
			return ConHash(hash_method=hash_method)
		else:
			return ConHash()

	def _init_method_conhash(self, config):
		self._name_pattern = config['name_pattern']

	def _update_method_conhash(self):
		addrs = self._service_dependency_manager.get_service_addrs(self._service_name)
		if len(addrs) == 0:
			return

		if addrs == self._addrs:
			return

		# from common.logger import log
		# log.debug('dynamic_distribution_cache|new_addrs=%s,old_addrs=%s', addrs, self._addrs)
		self._addrs = addrs

		_client = {}
		_conhash = self._create_conhash()
		for index in xrange(len(addrs)):
			name = self._name_pattern % index
			addr = addrs[index]
			host, port = addr.split(':')
			port = int(port)
			config = self._client_config.copy()
			config.update({
				'host': host,
				'port': port,
			})
			_client[name] = create_cache_client(name, config)
			_client[name].config = config
			_conhash.add_node(str(name), config.get('replica', 32), index)

		self._client = _client
		self._conhash = _conhash

	def _init_method_mod_div(self, config):
		self._factor = config['factor']
		if self._method in ('mod', 'div'):
			self._regex = re.compile(config['key_regex'])

	def _update_method_mod_div(self):
		addrs = self._service_dependency_manager.get_service_addrs(self._service_name)
		if len(addrs) == 0:
			return

		if addrs == self._addrs:
			return

		# from common.logger import log
		# log.debug('dynamic_distribution_cache|new_addrs=%s,old_addrs=%s', addrs, self._addrs)
		self._addrs = addrs

		_client = {}
		for index in xrange(len(addrs)):
			addr = addrs[index]
			host, port = addr.split(':')
			port = int(port)
			config = self._client_config.copy()
			config.update({
				'host': host,
				'port': port,
			})
			_client[index] = create_cache_client(index, config)
			_client[index].config = config

		self._client = _client

	def _get_client_by_key_mod(self, key):
		self._update()
		return super(DynamicDistributionCache, self)._get_client_by_key_mod(key)

	def _get_client_by_key_div(self, key):
		self._update()
		return super(DynamicDistributionCache, self)._get_client_by_key_div(key)

	def _get_client_by_key_hash_mod(self, key):
		self._update()
		return super(DynamicDistributionCache, self)._get_client_by_key_hash_mod(key)

	def _get_client_by_key_hash_div(self, key):
		self._update()
		return super(DynamicDistributionCache, self)._get_client_by_key_hash_div(key)

	def _get_client_by_key_conhash(self, key):
		self._update()
		return super(DynamicDistributionCache, self)._get_client_by_key_conhash(key)

	def get(self, key, retry=True):
		client = self.get_client_by_key(key)
		if client is None:
			return None

		try:
			return client.get(key)
		except Exception as e:
			from common.logger import log
			if retry:
				log.warning('dynamic_cache_connect_failed|services=%s', self._service_dependency_manager.services())
				return self.get(key, retry=False)
			else:
				log.exception('dynamic_cache_connect_failed|services=%s', self._service_dependency_manager.services())
				raise e


_cache_classes['dynamic_distribution'] = DynamicDistributionCache


def _celery_new_redis_client(self, **params):
	if not self._client_capabilities['socket_connect_timeout']:
		params.pop('socket_connect_timeout', None)
	from django.conf import settings

	connection_pool = DynamicRedisConnectionPool(
		service_dependency_manager=settings.SERVICE_DEPENDENCY_MANAGER,
		service_name=settings.REDIS_SERVICE_NAME,
		max_connections=32,
		timeout=5)
	return self.redis.Redis(connection_pool=connection_pool)


def patch_celery():
	from celery.backends.redis import RedisBackend
	RedisBackend._new_redis_client = _celery_new_redis_client
