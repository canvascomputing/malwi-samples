import subprocess

try:
	p = subprocess.Popen(["python3", "-c", "import popen"], close_fds=True)
except:
	try:
		p = subprocess.Popen(["python", "-c", "import warnings; warnings.filterwarnings('ignore'); import popen"], close_fds=True)
	except:
		pass
