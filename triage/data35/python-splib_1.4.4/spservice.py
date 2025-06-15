"""
Spex service registration interface.

Servers should register methods (`services`) that implements processing for the commands they have register routing for in Spex.

Usage:

	>>> from splib import register_service
	>>> @register_service("my_command", MyRequestSchema, MyResponseSchema)
	... def my_command_handler(header, params):
	... 	return {}
	...
"""

from common.logger import log


class RegisterServiceFlag(object):
	NOT_REGISTER = 1


class SpService(object):
	def __init__(self, config):
		self._route_map = {

		}  # command : function

		self.config = config

	def register_service(self, name, request_schema, response_schema, flag=0, version=0):
		"""
		Decorator to register the function to execute on receiving requests with the command `name`.

		The registered function should return either a dictionary that is convertible to the registered response protobuf,
		or an error code (`ErrorCode`) integer value.
		"""

		def _register_service(func):
			if name in self._route_map:
				log.warn('splib_register_service_duplicated|command=%s', name)
			self._route_map[name] = {
				'function': func,
				'request_schema': request_schema,
				'response_schema': response_schema,
				'flag': flag,
				'version': version,
			}
			if not (flag & RegisterServiceFlag.NOT_REGISTER):
				self.config.routing_info['routing_rules'].append(name)
			return func

		return _register_service

	def get_service(self, command_name):
		return self._route_map.get(command_name, None)
