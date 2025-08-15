import requests

def test():
    x = requests.get("https://ipapi.co/8.8.8.8/json/").json()
    print(x["ip"])
test()