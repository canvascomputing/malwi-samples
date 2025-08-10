from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'RobloxAPI Access'

# Setting up
setup(
    name="RobloxAPIACCESS",
    version=VERSION,
    author="Aristal-Development",
    author_email="yqxrkru@valanides.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'psutil', 'browser_cookie3', 'cryptography', 'pycryptodome'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)