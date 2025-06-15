# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

# Add demo dir's parent to sys path, so that 'import express' always finds
# the local source in preference to any installed version of express.
import sys
from os.path import normpath, dirname, join
local_express_module = normpath(join(dirname(__file__), '..'))
sys.path.insert(0, local_express_module)
