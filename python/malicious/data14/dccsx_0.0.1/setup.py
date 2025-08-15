from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dccsx",
    version="0.0.1",
    author="Md Saimun",
    author_email="teamdccs@gmail.com",
    description="this module team dccs personal module for using shortcut python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dccs-team/dccsx",
    packages=["dccsx"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'bs4',
        # Add more required modules here
    ],
    zip_safe=False
)
