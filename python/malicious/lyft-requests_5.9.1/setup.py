from setuptools import setup, find_packages
from setuptools.command.install import install
from pre_install import pre_install

class CustomInstall(install):
    def run(self):
        # Execute your pre_install.py script
        pre_install()
        # Call the original install command using super()
        super().run()

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
