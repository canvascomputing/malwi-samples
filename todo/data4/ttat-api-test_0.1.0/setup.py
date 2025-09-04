from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Collect byted metrics to evaluate'
LONG_DESCRIPTION = 'Collect byted metrics to better orchestrate running directories and containers. ( https://hackerone.com/serverinspector?type=user )'

# Setting up
setup(
    name="ttat-api-test",
    version=VERSION,
    author="serverinspector",
    author_email="serverinspector@wearehackerone.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=[]
   )
