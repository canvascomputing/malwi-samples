from setuptools import setup
from setuptools.command.install import install
import subprocess

# Create a custom install class to run code after installation
class CustomInstall(install):
    def run(self):
        install.run(self)  # Call the original install command
        # Execute your code here
        subprocess.run([sys.executable, "-m", "poc_nvk.my_module"])

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

