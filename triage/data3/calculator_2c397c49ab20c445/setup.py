from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1000.0.6'
DESCRIPTION = 'Dependecy Confusion POC'

# Setting up
setup(
    name="calculator_2c397c49ab20c445",
    version=VERSION,
    author="Zeyad Abulaban",
    author_email="zeyad.abuqasem@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
)

