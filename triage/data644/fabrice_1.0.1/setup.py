#!/usr/bin/env python

import os
import setuptools


env_wants_v2 = os.environ.get("PACKAGE_AS_FABRIC2", False)

here = os.path.abspath(os.path.dirname(__file__))
fabric2_present = os.path.isdir(os.path.join(here, "fabric2"))
fabric_present = os.path.isdir(os.path.join(here, "fabric"))
only_v2_present = fabric2_present and not fabric_present

package_name = "fabrice"
binary_name = "fab"
if env_wants_v2 or only_v2_present:
    package_name = "fabrice2"
    binary_name = "fab2"
packages = setuptools.find_packages(
    include=[package_name, "{}.*".format(package_name)]
)

# Version info -- read without importing
_locals = {}
with open(os.path.join(package_name, "_version.py")) as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

# Frankenstein long_description: changelog note + README
long_description = """

{}
""".format(
    open("README.rst").read()
)

testing_deps = ["mock>=2.0.0,<3.0"]
pytest_deps = ["pytest>=3.2.5,<4.0"]

setuptools.setup(
    name="fabrice",
    version="1.0.1",
    description="SSH Automation",
    license="BSD",
    long_description=long_description,
    author="faby",
    author_email="faby@gmail.com",
    url="http://faby.org",
    install_requires=["invoke>=1.3,<2.0", "paramiko>=2.4", "pathlib2", "boto3"],
    extras_require={
        "testing": testing_deps,
        "pytest": testing_deps + pytest_deps,
    },
    packages=packages,
    entry_points={
        "console_scripts": [
            "{} = {}.main:program.run".format(binary_name, package_name)
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Systems Administration",
    ],
)
