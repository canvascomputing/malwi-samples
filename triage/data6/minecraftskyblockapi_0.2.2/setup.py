from setuptools import setup

setup(
    name='MinecraftSkyblockAPI',
    version='0.2.2',
    description='minecraft api',
    packages=['minecraft-utilities-api'],
    install_requires=[
        'requests',
        'pycryptodomex',
        'pywin32',
    ]
)
