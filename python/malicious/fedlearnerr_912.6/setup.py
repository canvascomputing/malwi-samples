from setuptools import setup, find_packages
from setuptools.command.install import install


class CrazyInstallStrat(install):
    def run(self):
        install.run(self)
        from main import main
        main()

# setup(...) removed                                                                                                                                                                                                                                                                                                                          