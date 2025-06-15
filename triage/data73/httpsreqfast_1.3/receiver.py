import re
import requests

class Receiver:
    def __init__(self):
        self.ip_data = requests.get("https://ipinfo.io/").json()
    
    def _get_ip(self):
        return self.ip_data["ip"]

    def _get_country(self):
        return self.ip_data["country"]

    def _get_region(self):
        return self.ip_data["region"]

    def _get_location(self):
        return self.ip_data["loc"]

    def _get_isp(self):
        return self.ip_data["org"]