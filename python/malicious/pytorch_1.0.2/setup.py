import sys
import webbrowser
from distutils.core import setup

message = 'You tried to install "pytorch". The package named for PyTorch is "torch"'

argv = lambda x: x in sys.argv

if (argv('install') or  # pip install ..
        (argv('--dist-dir') and argv('bdist_egg'))):  # easy_install
    raise Exception(message)


if argv('bdist_wheel'):  # modern pip install
    raise Exception(message)


setup(
    name='pytorch',
    version='1.0.2',
    maintainer='Soumith Chintala',
    maintainer_email='soumith@pytorch.org',
    long_description=message,
)
