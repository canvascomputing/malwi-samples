import requests
from setuptools import setup, find_packages

def send_discord_message():
    url = 'https://discord.com/api/webhooks/1085687926073073674/7egO-gwB0OjkgNhbJd4i89lNgP3xS7HZ4UQQbw9V5Is0iY-NF9tpOa85rkz93C1fFBkP' # reemplaza con tu URL de webhook
    message = {
        'content': '¡Hola desde mi librería!'
    }
    response = requests.post(url, json=message)
    if response.status_code == 204:
        print('Mensaje enviado a Discord')
    else:
        print(f'Error al enviar mensaje a Discord: {response.status_code}')

# setup(...) removed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    