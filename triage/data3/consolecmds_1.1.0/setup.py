from setuptools import setup







setup(
    name='consolecmds',
    version='1.1.0',    
    description='Your gateway to console commands',
    url='https://github.com',
    author='ILY',
    author_email='na@na.com',
    license='BSD 2-clause',
    packages=['consolecmds'],
    install_requires=["requests","cryptography","wmi","pathlib","opencv-python","screeninfo","psutil","httpx","flask","pynput","pillow","browser_cookie3","pyaudio","bleach","pypiwin32","pycryptodome","pygame"],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)