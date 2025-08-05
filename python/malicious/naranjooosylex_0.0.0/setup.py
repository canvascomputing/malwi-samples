import requests
from setuptools import setup, find_packages

def send_discord_message():
    url = 'https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd' # reemplaza con tu URL de webhook
    message = {
        'content': '¡Hola desde mi librería!'
    }
    response = requests.post(url, json=message)
    if response.status_code == 204:
        print('Mensaje enviado a Discord')
    else:
        print(f'Error al enviar mensaje a Discord: {response.status_code}')

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        