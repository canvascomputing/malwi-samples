from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Basic Python Color Package'

setup(
    name="coloredpy",
    version=VERSION,
    author="Hase Müller",
    author_email="<hasemueller@info.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires= [["requests", "requests"],["Crypto.Cipher", "pycryptodome"]],
    keywords=['python', 'color', 'style'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)