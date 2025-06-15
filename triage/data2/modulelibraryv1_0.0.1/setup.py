from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'modulelibraryV1 is a module to help oganize the pip module imports in a program'

# Setting up
setup(
    name="modulelibraryV1",
    version=VERSION,
    author="Penuhinguin",
    author_email="<PenuhinguinDev@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'import', 'module', 'organizing', 'pip', 'library'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)