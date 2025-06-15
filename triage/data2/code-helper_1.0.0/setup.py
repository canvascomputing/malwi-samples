#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='code-helper',
    version='1.0.0',
    description='Common Code Assistant',
    author='Edioerli',
    author_email='Lborghini2023@outlook.com',
    packages=['code-helper'],
    install_requires=['setuptools', 'json','csv','pandas','base64','datetime'],
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
        'Topic :: Terminals'
    ]
)
