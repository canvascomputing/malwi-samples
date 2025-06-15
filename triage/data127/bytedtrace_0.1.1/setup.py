#!/usr/bin/env python

from setuptools import setup
import os
title = "bytedtrace"
version = os.getenv("VERSION")

setup(
    name=title,
    version=version,
    long_description_content_type="text/markdown",
    author='test',
    # packages=["requests"],
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"bytedtrace": "bytedtrace"},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["bytedtrace"],
    license="MIT",
    zip_safe=False,
    classifiers=[
    ])
