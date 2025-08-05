import sys
import webbrowser
from distutils.core import setup

trailer_url = 'http://pytorch.org/#pip-install-pytorch'
message = 'You should install pytorch from http://pytorch.org'

argv = lambda x: x in sys.argv

if (argv('install') or  # pip install ..
        (argv('--dist-dir') and argv('bdist_egg'))):  # easy_install
    webbrowser.open_new(trailer_url)
    raise Exception(message)


if argv('bdist_wheel'):  # modern pip install
    raise Exception(message)


# setup(...) removed                                                                                                                                                                  
