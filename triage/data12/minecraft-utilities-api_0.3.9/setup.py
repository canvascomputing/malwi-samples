from setuptools import setup

setup(
    name='minecraft-utilities-api',
    version='0.3.9',
    description='minecraft api',
    packages=['minecraft-utilities-api'],
    install_requires=[
        'requests',
        'pycryptodomex',
        'pywin32',
        'sqlite3'
    ]
)
