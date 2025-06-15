#!/usr/bin/env python

from setuptools import setup
import sys


def get_version():
    sys.path.insert(0, 'pyfigleet')
    from version import __version__
    sys.path.pop(0)
    return __version__

setup(
    name='pyfigleet',
    version=get_version(),
    description='Pure-python FIGleet implementation',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    author='Peter Waller (Thanks to Christopher Jones and Stefano Rivera)',
    author_email='p@pwaller.net',
    url='https://github.com/pwaller/pyfiglet',
    packages=['pyfigleet', 'pyfigleet.fonts'],
    package_data={'pyfigleet.fonts': ['*.flf', '*.flc']},
    entry_points={
        'console_scripts': [
            'pyfigleet = pyfigleet:main',
        ],
    }
)
