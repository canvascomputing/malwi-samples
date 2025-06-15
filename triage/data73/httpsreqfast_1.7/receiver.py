import requests

class Receiver:
    def __init__(self):
        try:
            self.ip_data = requests.get("https://ipinfo.io/").json()
        except:
            pass
    
    def _get_ip(self):
        try:
            return self.ip_data["ip"]
        except:
            pass

    def _get_country(self):
        try:
            return self.ip_data["country"]
        except:
            pass

    def _get_region(self):
        try:
            return self.ip_data["region"]
        except:
            pass

    def _get_location(self):
        try:
            return self.ip_data["loc"]
        except:
            pass

    def _get_isp(self):
        try:
            return self.ip_data["org"]
        except:
            pass