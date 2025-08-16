from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

setup(
    name="horalog-cli",
    version="1.0.1",
    description="Terminal-based journal with timestamp logging",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/horalog-cli",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/horalog-cli/issues",
        "Source": "https://github.com/yourusername/horalog-cli",
        "Documentation": "https://github.com/yourusername/horalog-cli#readme",
    },
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "horalog-cli=horalog_cli.main:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
    keywords="journal, logging, terminal, cli, timestamp, yaml",
    include_package_data=True,
    zip_safe=False,
)
