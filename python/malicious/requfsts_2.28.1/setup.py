from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

about = {}
about['__title__'] = "requfsts"
about['__description__'] = "Python HTTP for Humans."
about['__url__'] = "https://requests.readthedocs.io"
about['__version__'] = "2.28.1"
about['__build__'] = 0x022801
about['__author__'] = "Kenneth Reitz"
about['__author_email__'] = "me@kennethreitz.org"
about['__license__'] = "Apache 2.0"
about['__copyright__'] = "Copyright 2022 Kenneth Reitz"
about['__cake__'] = "\u2728 \U0001f370 \u2728"

requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<1.27",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==0.0.7",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=["requfsts"],
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"requests": "requests"},
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    tests_require=test_requirements,
    extras_require={
        "security": [],
        "socks": ["PySocks>=1.5.6, !=1.5.7"],
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],
    },
    project_urls={
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
