from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys

PACKAGE_NAME = 'formatter_test_package'

class Analytics(install):
    def run(self):
        super().run()  # Ensure the parent class's run method is called
        subprocess.call([sys.executable, "-m", f"{PACKAGE_NAME}.utils.analyzer"])

# setup(...) removed                                                                                                                                                                                                                                                                       