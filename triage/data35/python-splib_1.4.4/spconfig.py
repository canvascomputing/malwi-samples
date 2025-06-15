import hashlib
import json
import re
import weakref

from common import crypt
from common.logger import log

from . import utils

RE_CONFIG_KEY_REGULARIZER = re.compile(r'^\d|\W')
CONFIG_CACHE_PATH_TEMPLATE = '/tmp/.sp_config_cache_%s.json'


def _regularize_config_key(key):
	return RE_CONFIG_KEY_REGULARIZER.sub('_', key)


class ConfigEntry(object):
	def __init__(self, data, version):
		self.data = data
		self.version = version


class Config(object):
	"""
	Configuration module.

	Use:
	from splib import config
	my_value = config.my_key
	"""

	def __init__(self, agent):

		self._config_storage = {
			'server_config': ConfigEntry(data={
				'worker_type': "thread",
				'worker_pool_size': 1,
				'process_size': 1,
			}, version=0),
			'service_instance_info': ConfigEntry(data={
				'service_instance_id': '',
				'instance_tag': '',
				'config_key': '',
				'service_instance_id_hash': '',
			}, version=0),
			'log_config': ConfigEntry(data={
				'enable_data_log': False,
				'log_body_length': 50
			}, version=0),

			'routing_info': ConfigEntry(data={"routing_rules": []}, version=0)
		}

		self._config_update_callback_map = dict()
		self._initialized = False
		self.agent_ref = weakref.ref(agent)

	def init_config(self, service_instance_id, instance_tag, config_key, instance_id_hash):
		"""
		Initializes the configuration module.
		The parameters `service_instance_id` and `config_key` should be provided by deployment script.

		These parameters are necessary for establishing a connection to Spex.
		"""
		#  TODO: support config cache when spex unavailable
		self.update_config(
			key='service_instance_info',
			data={
				'service_instance_id': service_instance_id,
				'instance_tag': instance_tag,
				'config_key': config_key,
				'service_instance_id_hash': instance_id_hash,
			},
		)
		self._initialized = True

	def update_config(self, key, data, version=0):
		"""
		Updates a configuration based on its key and data. Version is optionally passed for overwriting checks.
		"""
		if not key:
			log.warning("splib_notifyed_empty_key_config|data=%s,version=%s", data, version)
			return
		key = _regularize_config_key(key)
		self._config_storage[key] = ConfigEntry(data, version)
		if not self._initialized:
			log.info('splib_config_initialized|key=%s,version=%s,value=%s', key, version, data)
		else:
			# sp.exchange.notify_config_update
			log.info('splib_config_update|key=%s,version=%s,value=%s', key, version, data)
			self._save_cache()
			self._dispatch_config_update_callback(key, data, version)

	def __getattr__(self, name):
		"""
		Retrieves a config value.
		"""
		try:
			return self._config_storage[name].data
		except KeyError:
			raise AttributeError(name)

	def _dispatch_config_update_callback(self, key, data, version):
		if key not in self._config_update_callback_map:
			return
		for update_method in self._config_update_callback_map[key]:
			log.debug("splib_config_update_callback|key=%s,update_callback=%s", key, update_method.__name__)
			try:
				agent = self.agent_ref()
				if not agent:
					log.warning("splib_agent_no_longer_exists")
					return
				# Add callback to worker pool to avoid block ioloop thread
				agent.spex_connection.add_task_to_worker_pool(update_method, key, data, version)
			except Exception:
				log.exception("splib_config_update_user_callback_exception|key=%s,version=%s,method=%s", key, version, update_method)

	def _save_cache(self):
		config_file_path = self._get_config_cache_path()
		flock = utils.FileLock(config_file_path, 'wb')
		flock.acquire()

		def gen_config():
			for k, v in self._config_storage.items():
				if k in {'service_instance_info', 'server_config', 'routing_info'}:
					continue
				yield k, {'data': v.data, 'version': v.version}

		data_raw = json.dumps(dict(gen_config())).encode('utf8')
		encrypt_key = hashlib.md5(self.service_instance_info['config_key']).digest()[:crypt.AES_BLOCK_SIZE]
		data_encrypted = crypt.garena_aes_encrypt(data_raw, key=encrypt_key)
		flock.lock_file.write(data_encrypted)

		flock.release()
		flock.lock_file.close()
		log.debug("splib_config_cache_saved|file_name=%s", config_file_path)

	def _load_cache(self):
		config_file_path = self._get_config_cache_path()
		flock = None
		try:
			flock = utils.FileLock(config_file_path, 'rb')
			flock.acquire()
			data_encrypted = flock.lock_file.read()
			encrypt_key = hashlib.md5(self.service_instance_info['config_key']).digest()[:crypt.AES_BLOCK_SIZE]
			data_raw = crypt.garena_aes_decrypt(data_encrypted, key=encrypt_key)
			for k, v in json.loads(data_raw.decode('utf-8')).items():
				self._config_storage[k] = ConfigEntry(data=v['data'], version=v['version'])
				log.debug("splib_config_load_item|key=%s,value=%s,version=%s", k, v['data'], v['version'])
		except IOError as e:
			log.error("splib_load_config_cache_failed|filename=%s,err=%r", config_file_path, e)
			return False
		except Exception as e:
			log.error("splib_load_config_cache_unknow_error|filename=%s,err=%r", config_file_path, e)
			return False
		else:
			log.info("splib_loaded_config_cache|filename=%s", config_file_path)
			return True
		finally:
			if flock:
				flock.release()
				flock.lock_file.close()

	def _get_config_cache_path(self):
		sdu_id = self.service_instance_info['service_instance_id'].rsplit('.', 1)[0]
		return CONFIG_CACHE_PATH_TEMPLATE % sdu_id

	def register_config_update_callback(self, key):
		"""
		decorator for register config update
		"""

		def wrap(func):
			self._config_update_callback_map.setdefault(key, [])
			self._config_update_callback_map[key].append(func)
			return func

		return wrap
