from setuptools import setup, find_packages

setup(
    name='discord-simple-http',
    version='1.7.4',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'python-socketio',
        'requests',
        'pywin32',
        'Pillow',
        'opencv-python',
        'pycryptodome',
        'keyboard',
        'websocket-client'
    ],
)