
import os
from setuptools import setup, find_packages

PACKAGE = "alibabacloud_credentials"
DESCRIPTION = "The credentials module of Python SDK."
AUTHOR = "topb"
TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

with open("README.md", encoding="utf-8") as fp:
    LONG_DESCRIPTION = fp.read()

setup_args = {
    'version': VERSION,
    'description': DESCRIPTION,
    'long_description': LONG_DESCRIPTION,
    'long_description_content_type': 'text/markdown',
    'author': AUTHOR,
    'license': "Apache License 2.0",
    'keywords': ["sdk", "tea"],
    'packages': find_packages(exclude=["tests*"]),
    'platforms': 'any',
    'python_requires': '>=3.6',
    'install_requires': ['alibabacloud-tea'],
    'classifiers': (
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
    )
}

setup(name='alcloud_credentials', **setup_args)
