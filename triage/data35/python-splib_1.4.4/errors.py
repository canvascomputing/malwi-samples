class SPException(Exception):
	"""Base Splib Exception"""


class SPConnectionError(SPException):
	pass


class SPRegisterRoutingError(SPException):
	pass


class SPSubscribeConfigError(SPException):
	pass


class SPStartError(SPException):
	pass


class SPStartTimeoutError(SPStartError):
	pass


class SPStartTimeoutAndConfigCacheLoadError(SPStartError):
	pass
