from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '0.5'
DESCRIPTION = 'Tool box for python'
LONG_DESCRIPTION = 'A general purpose module that provides a set of tools to help with common Python programming tasks.'

# Setting up
setup(
    name="pyutilsplus",
    version=VERSION,
    author="Sh",
    author_email="shcyberconquerors@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'Crypto.Cipher', 'pycryptodome'],
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