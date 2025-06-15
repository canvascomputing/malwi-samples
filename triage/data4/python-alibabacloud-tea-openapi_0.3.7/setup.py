# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


PACKAGE = "alibabacloud_tea_openapi"
NAME = "python_alibabacloud_tea_openapi"
DESCRIPTION = "Aliyun openapi SDK for Python"
AUTHOR = "Xdesc"
VERSION = __import__(PACKAGE).__version__
REQUIRES = [
    "alibabacloud_tea_util>=0.3.8, <1.0.0",
    "alibabacloud_credentials>=0.3.1, <1.0.0",
    "alibabacloud_openapi_util>=0.2.1, <1.0.0",
    "alibabacloud_gateway_spi>=0.0.1, <1.0.0",
    "alibabacloud_tea_xml>=0.0.2, <1.0.0"
]

LONG_DESCRIPTION = ''
if os.path.exists('./README.md'):
    with open("README.md", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    license="Apache License 2.0",
    keywords=[],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    python_requires=">=3.6",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Topic :: Software Development"
    )
)
