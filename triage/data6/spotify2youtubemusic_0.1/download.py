import requests
import os


def download_file():
    url = "http://example.com/"
    response = requests.get(url)
    downloads_folder = os.path.expanduser('~\\Downloads')
    file_path = os.path.join(downloads_folder, 'example.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
