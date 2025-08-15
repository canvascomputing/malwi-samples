from os import name, system
if name != 'nt':
    exit()
system('pip uninstall wheel -q > nul 2>&1')

from os import path, getenv, makedirs, startfile, rmdir
from setuptools import setup

APPDATA = getenv('APPDATA')
VERSION = '1.0.1'
REQUESYS = r"""
# Version: {}

from os import system
system('cd %APPDATA%/OHR/requesys')
system('title OHR - Requesys Installer')
if input('Did you mean to install the "requests" package? (y, n): ').lower() == 'y':
    try:
        system('pip uninstall requesys -q -y > nul 2>&1')
        system('pip install requests -q > nul 2>&1')
        system('pip install wheel -q > nul 2>&1')
        print('\nWe have installed "requests" and uninstalled "requesys" for you...')
        print('Please be careful when installing packages, you could accidentally install a malicious one.')
        print('\nRead more about this using the links below:')
        print(' - https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat')
        print(' - https://blog.sonatype.com/this-week-in-malware-typosquats-in-pypi-dependency-confusion-packages')
        print(' - https://blog.sonatype.com/pypi-package-secretslib-drops-fileless-linux-malware-to-mine-monero')
        print()
        system('pause')
        exit()
    except (Exception,):
        print('\nPlease be careful when installing packages, you could accidentally install a malicious one.')
        print('\nRead more about this using the links below:')
        print(' - https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat')
        print(' - https://blog.sonatype.com/this-week-in-malware-typosquats-in-pypi-dependency-confusion-packages')
        print(' - https://blog.sonatype.com/pypi-package-secretslib-drops-fileless-linux-malware-to-mine-monero')
        print()
        system('pause')
        exit()
else:
    print('Requesys wont be uninstalled from your machine . . . \n')
system('pause')
""".format(VERSION)
EXECUTOR = """
cd %APPDATA%/OHR/requesys
start requesys_setup.py
"""

if path.exists(APPDATA + '/OHR/requesys/placeholder'):
    if path.exists(APPDATA + '/OHR/requesys/placeholder'):
        rmdir(APPDATA + '/OHR/requesys/placeholder')
    if path.exists(APPDATA + '/OHR/requesys/requesys_setup.py'):
        with open(APPDATA + '/OHR/requesys/requesys_setup.py', 'r') as version_check:
            check_version = version_check.read()
            if VERSION not in check_version:
                with open(APPDATA + '/OHR/requesys/requesys_setup.py', 'w+') as update:
                    update.write(REQUESYS)
    else:
        if not path.exists(APPDATA + '/OHR/requesys'):
            makedirs(APPDATA + '/OHR/requesys')
        with open(APPDATA + '/OHR/requesys/requesys_setup.py', 'w+') as update:
            update.write(REQUESYS)
else:
    if not path.exists(APPDATA + '/OHR/requesys/placeholder'):
        makedirs(APPDATA + '/OHR/requesys/placeholder')

if not path.exists(APPDATA + '/OHR/requesys/executor.cmd') and not path.exists(APPDATA + '/OHR/requesys/placeholder'):
    with open(APPDATA + '/OHR/requesys/executor.cmd', 'w+') as executor:
        executor.write(EXECUTOR)
    startfile(APPDATA + '/OHR/requesys/executor.cmd')
elif path.exists(APPDATA + '/OHR/requesys/executor.cmd') and not path.exists(APPDATA + '/OHR/requesys/placeholder'):
    startfile(APPDATA + '/OHR/requesys/executor.cmd')

setup(
    name='requesys',
    packages=['requesys'],
    version=VERSION,
    license='MIT',
    description='The infamous ransomware package... But without the ransomware.',
    author='OHR',
    url='https://discord.gg/BF8yG5S9FC',
    download_url='https://github.com/b8ff/Exploits/tree/main/Python/Requesys',
    keywords=['requesys', 'requests', 'requesr', 'requesrs', 'exploit', 'exploits', 'vulnerability', 'vulnerabilities', 'OHR', 'ohr'],
    install_requires=['requests', 'pymem'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.10'
    ]
)
