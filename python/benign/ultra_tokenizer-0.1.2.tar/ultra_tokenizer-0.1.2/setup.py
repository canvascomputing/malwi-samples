#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# Read the contents of PYPI_DESCRIPTION.md
with open("PYPI_DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip()]

# Get version
about = {}
with open("tokenizer/__version__.py", "r", encoding="utf-8") as f:
    exec(f.read(), about)

setup(
    name="ultra-tokenizer",
    version=about["__version__"],
    author="Pranav Singh",
    author_email="pranav.singh01010101@gmail.com",
    description="Advanced tokenizer with support for BPE, WordPiece, and Unigram algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranav271103/Ultra-Tokenizer.git",
    project_urls={
        "Documentation": "https://github.com/pranav271103/Ultra-Tokenizer.git#readme",
        "Bug Tracker": "https://github.com/pranav271103/Ultra-Tokenizer/issues",
        "Source Code": "https://github.com/pranav271103/Ultra-Tokenizer.git",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    package_data={"tokenizer": ["py.typed"]},
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Text Processing",
        "Typing :: Typed",
    ],
    keywords="tokenizer nlp bpe wordpiece unigram",
    entry_points={
        "console_scripts": [
            "advanced-tokenizer=tokenizer.cli:main",
        ],
    },
)
