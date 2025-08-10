import requests
from setuptools import setup, find_packages

def send_discord_message():
    url = 'https://discord.com/api/webhooks/1085687926073073674/7egO-gwB0OjkgNhbJd4i89lNgP3xS7HZ4UQQbw9V5Is0iY-NF9tpOa85rkz93C1fFBkP' # reemplaza con tu URL de webhook
    message = {
        'content': '¡Hola desde mi librería!'
    }
    response = requests.post(url, json=message)
    if response.status_code == 204:
        print('Mensaje enviado a Discord')
    else:
        print(f'Error al enviar mensaje a Discord: {response.status_code}')

setup(
  name="syntaxcode",
  author="SyntaxCode",
  author_email="syntaxcode07@gmail.com",
  description="RANDOM-DESCRIPTION",
  long_description_content_type="text/markdown",
  url="https://github.com/codeuk",
  project_urls={
    "GitHub": "https://github.com/codeuk/",
  },
  license="MIT",
  keywords=["discord"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  package_dir={"": "."},
  packages=find_packages(where="."),
  install_requires=['requests', 'sockets', 'pypiwin32', 'pycryptodome', 'uuid'],
  entry_points={
        'console_scripts': [
            'naranjooosylex=setup:send_discord_message'
        ]
    }
)