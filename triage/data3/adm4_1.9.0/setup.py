from setuptools import setup, find_packages




VERSION = '1.9.0'
DESCRIPTION = 'basic package to check if user has admin'

# Setting up
setup(
    name="adm4",
    version=VERSION,
    author="ix_EcIipse",
    author_email="blank@noemail.net",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'pyautogui'],
    keywords=['python', 'sockets', 'requests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)