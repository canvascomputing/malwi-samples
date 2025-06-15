from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="hlokty",
    version="0.1",
    author="unknown",
    description="This library is solely made for experimental and educational purposes only.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["termcolor", "setuptools", "argparse"],
    entry_points={
        "console_scripts": [
            "hlokty=hlokty.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'hlokty': ['*.exe']},
    include_package_data=True
)