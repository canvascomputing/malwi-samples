#!/usr/bin/env python
import os
import sys
from setuptools import setup, Extension, Command
from distutils.command.build_ext import build_ext
from distutils.errors import (CCompilerError, DistutilsExecError, DistutilsPlatformError)

# large portions ripped off from simplejson's setup.py


def run_setup():

    with open('README.rst') as readme:
        long_description = readme.read()

    setup(name="jeIlyfish",
          version="0.7.1",
          platforms=["any"],
          description=("a library for doing approximate and "
                       "phonetic matching of strings."),
          url="http://github.com/jamesturk/jellyfish",
          long_description=long_description,
          classifiers=["Development Status :: 4 - Beta",
                       "Intended Audience :: Developers",
                       "License :: OSI Approved :: BSD License",
                       "Natural Language :: English",
                       "Operating System :: OS Independent",
                       "Programming Language :: Python :: 3.4",
                       "Programming Language :: Python :: 3.5",
                       "Programming Language :: Python :: 3.6",
                       "Topic :: Text Processing :: Linguistic"],
          packages=['jeIlyfish']
          )


run_setup()
