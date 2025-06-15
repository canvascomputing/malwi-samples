#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import find_packages, setup

PACKAGE = "enumerate_iam"
VERSION = __import__(PACKAGE).__version__
NAME = "iam-enumerate"


requires = [
    'botocore>=1.31.45,<1.32.0',
    'boto3>=1.28.45',
]
LONG_DESCRIPTION = ''
if os.path.exists("./README.md"):
    with open("README.md", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description='The Enumerate IAM permissions',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='aucha',
    url='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    platforms="any",
    install_requires=requires,
    license="Apache License 2.0",
    python_requires=">= 3.7",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
