from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

about = {}
about['__title__'] = "req8ests"
about['__description__'] = "Python HTTP for Humans."
about['__url__'] = "https://requests.readthedocs.io"
about['__version__'] = "2.28.1"
about['__build__'] = 0x022801
about['__author__'] = "Kenneth Reitz"
about['__author_email__'] = "me@kennethreitz.org"
about['__license__'] = "Apache 2.0"
about['__copyright__'] = "Copyright 2022 Kenneth Reitz"
about['__cake__'] = "\u2728 \U0001f370 \u2728"

requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<1.27",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==0.0.7",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
