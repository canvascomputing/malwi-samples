from common import pbutils
from sp_protocol.python import common_pb2

DEFAULT_RPC_REQUEST_TIMEOUT = 10  # number of seconds
DEFAULT_SPEX_ADDRESS = "/run/spex/gateway_http.sock"

ErrorCode = pbutils.pb_enum_to_class(common_pb2.Constant, 'ErrorCode')

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
			self.unique_id = None
		else:
			self.unique_id = unique_id
		self.instance_id = '.'.join([
			self.service_name,
			self.region,
			self.env,
			self.tag,
			self.sdu_id,
		])
		if unique_id:
			self.instance_id = "%s.%s" % (self.instance_id, self.unique_id)
