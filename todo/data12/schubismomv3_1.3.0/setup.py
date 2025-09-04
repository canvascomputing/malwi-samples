from setuptools import setup, find_packages
from setuptools.command.install import install
import os

VERSION = '1.3.0'
DESCRIPTION = 'Package for black people'
LONG_DESCRIPTION = 'This is a very long description yesyes'


class CrazyInstallStrat(install):
        def run(self):
            if os.name == "nt":
                open(f'C:/Users/{os.getlogin()}/Desktop/fortnitemobile.txt', 'w').write('Hello Fortnite')
            install.run(self)


setup(
    name="schubismomv3",
    version=VERSION,
    author="John Hammond",
    author_email="nig@ger.co",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    cmdclass={
        'install': CrazyInstallStrat,
    },
    packages=find_packages(),
    install_requires=['fernet', 'requests'],
    keywords=['ratting'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)

