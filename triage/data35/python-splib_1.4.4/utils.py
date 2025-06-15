import hashlib
import os
import fcntl
import time
import threading
import tornado.ioloop
from tornado import gen

from common.logger import log
from sp_protocol.python import common_pb2

ErrorCodeMap = {v: k for k, v in common_pb2.Constant.ErrorCode.items()}


def get_timestamp_us():
	return int(time.time() * 1000000)


def time_after_seconds(seconds):
	return time.time() + seconds


def try_setup_resolver():
	try:
		import tornado.util  # pylint:disable=redefined-outer-name
		resolver = tornado.util.import_object('tornado.platform.caresresolver.CaresResolver')
		import tornado.netutil
	except ImportError:
		return
	else:
		tornado.netutil.Resolver.configure(resolver)
		log.info('splib_splib_resolver_configure_suceess')


def call_coroutine(corutine_func, *args, **kwargs):
	ioloop = kwargs.pop('ioloop', tornado.ioloop.IOLoop.current())
	timeout_result = kwargs.pop('timeout_result', None)
	event = threading.Event()
	rv = {
		'value': timeout_result
	}

	@gen.coroutine
	def cb():
		try:
			rv['value'] = yield corutine_func(*args, **kwargs)
		except Exception as e:
			log.exception("splib_thread_call_coroutine_exception|error=%r", e)
		event.set()

	ioloop.add_callback(cb)
	event.wait()
	return rv['value']


def get_error_code_msg(error_code):
	return ErrorCodeMap.get(error_code, 'UNKNOW_ERROR')


def parse_instance_tag_from_environment():
	sp_instance_tag = os.getenv('SP_INSTANCE_TAG')
	if not sp_instance_tag:
		return 'test', 'master'
	env, tag = sp_instance_tag.partition('.')[::2]
	# if only one word, it is env
	if not env:
		env = 'test'
	if not tag:
		tag = 'master'
	return env, tag


def service_instance_id_hash(service_instance_id):
	return hashlib.md5(service_instance_id.encode()).digest()[-4:]


class FileLock:
	"""
		Implements a file-based lock using flock(2).
	"""

	def __init__(self, file_path, mode):
		self.lock_file = open(file_path, mode)

	def acquire(self, blocking=True):
		"""Acquire the lock.
		If the lock is not already acquired, return None.  If the lock is
		acquired and blocking is True, block until the lock is released.  If
		the lock is acquired and blocking is False, raise an IOError.
		"""
		ops = fcntl.LOCK_EX
		if not blocking:
			ops |= fcntl.LOCK_NB
		fcntl.flock(self.lock_file, ops)

	def release(self):
		"""Release the lock. Return None even if lock not currently acquired"""
		fcntl.flock(self.lock_file, fcntl.LOCK_UN)
