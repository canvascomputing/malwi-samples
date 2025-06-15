from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.5'
DESCRIPTION = 'test'
LONG_DESCRIPTION = 'Learning stuff or whatever'

# Setting up
setup(
    name="ttat-api",
    version=VERSION,
    author="serverinspector2",
    author_email="serverinspector+2@wearehackerone.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=[]
   )
