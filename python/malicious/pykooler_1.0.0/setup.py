from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path



VERSION = '1.0.0'
DESCRIPTION = 'Cool package.'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


class InstallCommand(install):

    def run(self):
        try:
            print("Installing..")
        except:
            pass
        install.run(self)


# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   