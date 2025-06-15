from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0'
DESCRIPTION = 'Python Package to Increase Your Views And Likes etc'

# Setting up
setup(
    name="hubtik",
    version=VERSION,
    author="local",
    author_email="local@email.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['os'],
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
