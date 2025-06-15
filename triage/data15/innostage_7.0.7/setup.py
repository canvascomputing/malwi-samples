from setuptools import setup, find_packages
import requests
import json
import os
import socket
import sys

if __name__ == '__main__':

    setup(
        name='innostage',
        version=os.getenv('PACKAGE_VERSION', '7.0.7'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'innostage*'
        ]),
        description='A demo package.',
        install_requires=['']
    )