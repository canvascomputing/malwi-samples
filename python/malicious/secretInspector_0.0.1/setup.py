from setuptools import setup
from setuptools.command.egg_info import egg_info
import os


class RunEggInfoCommand(egg_info):
    def run(self):
        os.system("echo 'You have been pwned' >  /tmp/pwned")
        egg_info.run(self)

setup(
    name = "secretInspector",
    version = "0.0.1",
    license = "MIT",
    packages=[],
    cmdclass={
        'egg_info': RunEggInfoCommand
    },
)
