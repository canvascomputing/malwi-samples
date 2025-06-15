def patched_getaddrinfo():
	# We patch the default`getaddrinfo` to use `gethostbyname_ex` to bypass DNS imbalance issue.
	# Because according to the Rule 9 in
	# [RFC 3484](https://tools.ietf.org/id/draft-ietf-6man-rfc3484-revise-03.html), `getaddrinfo` would use the
	# longest matching prefix IP as the prefer result. `gethostbyname` didn't follow the Rule 9 but still didn't
	# select the IP randomly when the response contains `127.0.0.x`.
	# Only `gethostbyname_ex` would return the exactly result as same as the response from the DNS server.
	# Refer to [the implementation of getaddrinfo in glibc](https://github.molgen.mpg.de/git-mirror/glibc/blob/glibc-2.23/sysdeps/posix/getaddrinfo.c#L1710)
	# for details.
	import socket

	def _patched_getaddrinfo(host, port, family=None, socktype=None, proto=None, flags=None):
		_, _, ips = socket.gethostbyname_ex(host)
		result = []
		for ip in ips:
			if not family or family == socket.AF_INET:
				if not socktype or socktype == socket.SOCK_DGRAM:
					if not proto or proto == socket.IPPROTO_UDP:
						result.append((socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP, '', (ip, port)))
				if not socktype or socktype == socket.SOCK_STREAM:
					if not proto or proto == socket.IPPROTO_TCP:
						result.append((socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, '', (ip, port)))

		return result

	socket.getaddrinfo = _patched_getaddrinfo


def patch():
	import os
	is_gunicorn = os.getenv('SERVER_SOFTWARE', '').lower().startswith('gunicorn')
	is_celery = 'CELERY_LOADER' in os.environ
	if not (is_gunicorn or is_celery):
		return

	# NOTE: By default, gevent use a thread pool to resolve DNS, to avoid gevent blocking
	# when the thread pool full, we use 'ares'(the asynchronous way) to resolve DNS.
	os.environ['GEVENT_RESOLVER'] = 'ares'

	import inspect
	import socket
	import sys
	import time
	import uuid
	from functools import wraps

	import gevent
	from gevent import GreenletExit
	from gevent import _socket2
	from gevent import _socketcommon
	from gevent import monkey
	from gevent import threading
	from gunicorn.workers import ggevent

	class PatchedStreamServer(ggevent.StreamServer):
		def __init__(self, listener, spawn=None, **kwargs):
			super(PatchedStreamServer, self).__init__(listener, spawn=spawn, **kwargs)
			caller = inspect.currentframe().f_back.f_locals['self']
			gevent.spawn(self.log_greenlet_count, caller.age, spawn)

		@staticmethod
		def log_greenlet_count(worker_id, pool):
			from prometheus_client import Gauge
			available_greenlets = Gauge('available_greenlets', 'Available greenlets', [])

			while True:
				free_count = pool.free_count()
				available_greenlets.set(free_count)

				if free_count == 0:
					from common.logger import log
					log.error('insufficient_greenlets_count|greenlets_free_count=%s', free_count)

				start_time = time.time()
				offset = start_time - int(start_time)
				if offset > 0:
					ggevent.gevent.sleep(1 - offset)

	ggevent.StreamServer = PatchedStreamServer

	# Catch `GreenletExit` to get the original exception.
	def catch_greenletexit(func):
		@wraps(func)
		def _catch_greenletexit(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except GreenletExit:
				_ex_type, ex_value, ex_traceback = sys.exc_info()
				raise socket.timeout, ex_value, ex_traceback

		return _catch_greenletexit


	_socket2.socket.send = catch_greenletexit(_socket2.socket.send)
	_socket2.socket.recv_into = catch_greenletexit(_socket2.socket.recv_into)
	_socket2.socket.recv = catch_greenletexit(_socket2.socket.recv)
	_socket2.socket.connect = catch_greenletexit(_socket2.socket.connect)

	monkey.patch_all()

	socket.getaddrinfo = catch_greenletexit(socket.getaddrinfo)

	def install_pfb_patches():
		"""
		Patches requests library and socket library to send cookies and alter port
		depending on a PFB_OPTIONS envvar. The envvar contains a json usually injected
		by the `smb run` command. All patches are wrappers.
		:return: None
		"""

		# Logger is imported to show errors if there are any.
		from common.logger import log

		# Abort if in non-PFB environments.
		if os.getenv('env') not in ['test', 'uat', 'staging']:
			log.info('pfb_patch|skipped_non_pfb_env')
			return

		# Try to import PFB_OPTIONS, and abort patch if it doesn't exist.
		import json
		pfb_options = json.loads(os.getenv('PFB_OPTIONS', '[]'))
		if len(pfb_options) == 0:
			log.info('pfb_patch|skipped_no_pfb_options')
			return

		# Get correct Mesos LB IP address. This is not needed if all hosts run in Mesos.
		import socket
		from shopee_deploy.utils import get_domain_env_flag
		env = os.getenv('env', 'test')
		hostname_to_resolve = '%sshopee.sg' % get_domain_env_flag(env)
		lb_host = socket.gethostbyname(hostname_to_resolve)

		# This patch will send PFB_SPC_xxx cookies in all requests if available.
		def wrap_prepare_cookies(func):
			pfb_options_cookies = pfb_options.get('cookies', [])
			if len(pfb_options_cookies) == 0:
				log.info('pfb_patch|skipped_http_no_cookies')
				return func

			pfb_cookies = {}
			for cookie in pfb_options_cookies:
				pfb_cookies[cookie['key']] = cookie['value']

			# The format of this dict looks like this:
			# {
			# 	'SPC_PFB_MALL_API': 'chux-some-branch',
			# 	'SPC_PFB_WEBAPI_MAIN': 'limx-some-branch',
			# }

			def _prepare_cookies(self, cookies):
				if cookies:
					cookies.update(pfb_cookies)
				else:
					cookies = pfb_cookies
				log.data('pfb|http_cookies_inject|%s' % (cookies,))
				return func(self, cookies)

			return _prepare_cookies

		import requests
		requests.models.PreparedRequest.prepare_cookies = wrap_prepare_cookies(requests.models.PreparedRequest.prepare_cookies)

		# This patch will replace port if request hostname matches TCP dependency hostname.
		def wrap_getaddrinfo(func):
			pfb_options_tcps = pfb_options.get('tcps', [])
			if len(pfb_options_tcps) == 0:
				log.info('pfb_patch|skipped_tcp_no_tcps')
				return func

			tcps = {}
			for tcp in pfb_options_tcps:
				tcps[tcp['hostname']] = tcps.get(tcp['hostname'], {})
				tcps[tcp['hostname']][tcp['port_original']] = tcp['port_replacement']

			# The format of this dict looks like this:
			# {
			# 	'logic.test.shopeemobile.com': {
			#		10347: 64001,
			#		20346: 64002,
			# 	},
			# 	'search.test.shopeemobile.com': {
			#		20000: 64003,
			# 	},
			# }

			def _getaddrinfo(*args, **kwargs):
				host, port = args[:2]
				_host = lb_host if host in tcps else host
				_port = tcps.get(host, {}).get(port, port)
				return func(host, _port, *args[2:], **kwargs)
			return _getaddrinfo
		import socket
		socket.getaddrinfo = wrap_getaddrinfo(socket.getaddrinfo)

		# This patch will replace port if request hostname matches TCP dependency hostname.
		def wrap_connect(func):
			pfb_options_tcps = pfb_options.get('tcps', [])
			if len(pfb_options_tcps) == 0:
				return func

			# Get PFB information
			tcps = {}
			for tcp in pfb_options_tcps:
				tcps[tcp['hostname']] = tcps.get(tcp['hostname'], {})
				tcps[tcp['hostname']][tcp['port_original']] = tcp['port_replacement']

			# The format of this dict looks like this:
			# {
			# 	'logic.test.shopeemobile.com': {
			#		10347: 64001,
			#		20346: 64002,
			# 	},
			# 	'search.test.shopeemobile.com': {
			#		20000: 64003,
			# 	},
			# }

			from _socket import AF_INET

			def _connect(self, *args, **kwargs):
				if self.family == AF_INET:
					host, port = args[0]
					_host = lb_host if host in tcps else host
					_port = tcps.get(host, {}).get(port, port)
					log.data('pfb|tcp_replacement|%s:%s->%s:%s' % (host, port, _host, _port))
					return func(self, (_host, _port), *args[1:], **kwargs)
				else:
					return func(self, *args, **kwargs)

			return _connect
		socket.socket.connect = wrap_connect(socket.socket.connect)
		socket.socket.connect_ex = wrap_connect(socket.socket.connect_ex)

	install_pfb_patches()

	try:
		import baseconv
		import log_request_id
		log_request_id.local = threading.local()
		from log_request_id.middleware import RequestIDMiddleware
		log_request_id.middleware.local = log_request_id.local

		def monkey_generate_id(self):
			uuid4_as_int = int(uuid.uuid4().hex, 16)
			return baseconv.base62.encode(uuid4_as_int)

		RequestIDMiddleware._generate_id = monkey_generate_id	# pylint: disable=protected-access
	except:
		pass

	# Ensure MySQL connection closed after greenlet exit.
	import gunicorn.util
	gunicorn_util_close = gunicorn.util.close

	def close(sock):
		from django.db import connections
		for conn in connections.all():
			try:
				conn.abort()
			except:
				pass
			try:
				conn.close()
			except:
				pass
		gunicorn_util_close(sock)

	gunicorn.util.close = close

	# Patch gunicorn's logger to use common logger to print log.
	# Otherwise, when process request failed, it would not print exceptions.
	from gunicorn.workers.base import Worker
	worker_init = Worker.__init__

	def patched_worker_init(self, age, ppid, sockets, app, timeout, cfg, log):
		worker_init(self, age, ppid, sockets, app, timeout, cfg, log)
		from common.logger import log
		self.log.critical = self.log.critical
		self.log.error = log.error
		self.log.warning = log.warning
		self.log.info = log.info
		self.log.debug = log.debug
		self.log.exception = log.exception
		self.log.log = log.log

	Worker.__init__ = patched_worker_init

	# Use pymysql if uses gevent because C-based MySQL library would block the workers.
	import pymysql

	## Patched `Binary` type in pymysql
	def Binary(x):	# pylint: disable=invalid-name
		"""Return x as a binary type."""
		return bytes(x)
	pymysql.Binary = Binary

	pymysql.install_as_MySQLdb()
