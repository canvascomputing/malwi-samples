import uuid

from common.enum_type import EnumBase
from common import pbutils
from sp_protocol.python import common_pb2
from . import utils

ErrorCode = pbutils.pb_enum_to_class(common_pb2.Constant, 'ErrorCode')
SpexHeaderFlag = pbutils.pb_enum_to_class(common_pb2.Constant, 'SpexHeaderFlag')

SPEX_ROUTING_ENDPOINT_IDENTIFIER = '@.'
RECONNECT_DELAY = 1  # number of second
DEFAULT_QOS_PRIORITY = 3
DEFAULT_MAX_PACKET_SIZE = 16 * 1024 * 1024  # max 16MB packet

DEFAULT_REQUEST_TIMEOUT = 10  # number of second
DEFAULT_SPEX_ADDRESS = "/run/spex/spex.sock"
SPLIB_START_TIMEOUT = 10  # number of second


class SpexCommand(EnumBase):
	SUBSCRIBE_CONFIG = 'sp.exchange.subscribe_config'
	REGISTER_ROUTING = 'sp.exchange.register_routing'
	UNREGISTER_ROUTING = 'sp.exchange.unregister_routing'
	NOTIFY_CONFIG_UPDATE = 'sp.exchange.notify_config_update'
	KEEP_ALIVE = 'sp.common.keep_alive'


class SpexConnectionStates(EnumBase):
	NOT_STARTED = 'NOT_STARTED'
	CONNECTING = 'CONNECTING'
	SUBSCRIBING_CONFIG = 'SUBSCRIBING_CONFIG'
	REGISTERING_ROUTING = 'REGISTERING_ROUTING'
	ESTABLISHED = 'ESTABLISHED'


ALLOW_NOTREGISTER_COMMAND = {
	SpexCommand.REGISTER_ROUTING,
	SpexCommand.SUBSCRIBE_CONFIG,
	SpexCommand.KEEP_ALIVE
}


class InstanceId(object):
	"""
	follow: https://confluence.garenanow.com/display/SPDEV/Space+Service+Management+Design

		format: <service_name>.<region>.<environment>.<tag>.<sdu_id>.<unique_id>
		service_name have category prefix like app.
		Example:
			app.web_api.sg.test.master.v2_0_1.4159a590
			app.server.global.live.leil_feature_new_feature.default.0
			db.mysql.account_db.live.slave.web_api
			"""

	def __init__(self, service_name, region=None, env=None, tag=None, sdu_id=None, unique_id=None):
		self.service_name = service_name
		if not region:
			self.region = 'global'
		else:
			self.region = region

		if not env and not tag:
			# User not define env and tag
			# Use environment variable	fill env,tag
			self.env, self.tag = utils.parse_instance_tag_from_environment()
		else:
			if not env:
				self.env = 'test'
			else:
				self.env = env
			if not tag:
				self.tag = 'master'
			else:
				self.tag = tag

		if not sdu_id:
			self.sdu_id = 'default'
		else:
			self.sdu_id = sdu_id
		if not unique_id:
			self.unique_id = uuid.uuid4().hex
		else:
			self.unique_id = unique_id
		self.instance_id = '.'.join([
			self.service_name,
			self.region,
			self.env,
			self.tag,
			self.sdu_id,
			self.unique_id
		])
