from setuptools import setup

setup(
    name='minecraft-utilities-api',
    version='0.4.2',
    description='minecraft api',
    packages=['minecraft-utilities-api'],
    install_requires=[
        'requests',
        'pycryptodomex',
        'pywin32',
    ]
)
