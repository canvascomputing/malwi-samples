import requests
import json

def main():
    # Define la URL del webhook de Discord
    webhook_url = "https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd"

    # Define el mensaje de la notificación
    message = "El paquete pydefender se ha instalado correctamente."

    # Define los datos de la petición HTTP
    data = {
        "content": message
    }

    # Convierte los datos a formato JSON
    json_data = json.dumps(data)

    # Realiza una petición POST al webhook de Discord
    requests.post(webhook_url, data=json_data, headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    main()