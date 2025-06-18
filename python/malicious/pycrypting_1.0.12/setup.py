from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.12'
DESCRIPTION = 'Python Crypter For Red Teaming'

# Setting up
setup(
    name="pycrypting",
    version=VERSION,
    author="whoami (claysmith)",
    author_email="<claysmith@yahoo.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['termcolor', 'request', 'random'],
    keywords=['python', 'crypter', 'avbypass', 'crypt'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)
