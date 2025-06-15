

import os
import sys

import fantail

from . import kmeta

app = None

def dispatch():
    """
    invoke kea
    """
    global app

    app = fantail.app(name='kea3')
    app.discover(globals())
    app.discover(kmeta)
    app.run()
