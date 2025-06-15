import requests

class Receiver:
    def __init__(self):
        return
    
    def _get_ip(self):
        return requests.get("https://api.ipify.org/").text