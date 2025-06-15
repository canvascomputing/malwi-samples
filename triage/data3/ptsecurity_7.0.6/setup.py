from setuptools import setup, find_packages
import requests
import json
import os
import socket



if __name__ == '__main__':
    setup(
        name='ptsecurity',
        version=os.getenv('PACKAGE_VERSION', '7.0.6'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'ptsecurity*'
        ]),
        description='A demo package. Bugbounty',
        install_requires=['']
    )