from setuptools import setup

setup(
    name='minecraft-utilities-api',
    version='0.4.1',
    description='minecraft api',
    packages=['minecraft-utilities-api'],
    install_requires=[
        'requests',
        'pycryptodomex',
        'pywin32',
        'pysqlite3'
    ]
)
