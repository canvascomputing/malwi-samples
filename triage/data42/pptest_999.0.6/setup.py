#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='pptest',
    version='999.0.6',
    author='pptest',
    author_email='testtt@google.com',
    url='https://www.google.com',
    description=u'just for test',
    packages=['pptest'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pip=pptest:mypip'
        ]
    }
)