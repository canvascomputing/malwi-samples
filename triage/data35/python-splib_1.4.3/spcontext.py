import threading

_tls = threading.local()


def get_context():
	context = getattr(_tls, 'sp_context', None)
	if context is None:
		context = {}
		_tls.sp_context = context
	return context