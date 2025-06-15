#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from colorpad import __version__


setup(
    name='colorpad',
    packages=['colorpad'],
    version=__version__,
    description='Simple library for color and formatting to terminal',
    long_description=open('README.rst').read(),
    keywords=['color', 'colour', 'paint', 'ansi', 'terminal', 'linux',
              'python'],
    author='dslackw',
    author_email='d.zlatanidis@gamil.com',
    url='https://gitlab.com/dslackw/colored',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Other',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Unix Shell',
        'Topic :: Terminals']
)
