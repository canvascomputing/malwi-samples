from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstall(install):
    def run(self):
        install.run(self)
        subprocess.run([sys.executable, "-m", "poc_nvk.my_module"])

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

