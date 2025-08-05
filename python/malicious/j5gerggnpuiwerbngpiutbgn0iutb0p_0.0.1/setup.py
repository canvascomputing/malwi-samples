from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Dependency confusion Attack'
LONG_DESCRIPTION = 'Python package dependency confusion vulnerability POC. Impact of this vulnerability is Remote code execution (RCE)'

# Setting up
# setup(...) removed                                                                                                                                                                                                                                                                                                                                 
