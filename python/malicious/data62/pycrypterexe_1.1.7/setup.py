from setuptools import setup, find_packages

setup(
  name="pycrypterexe",
  version='1.1.7',
  author="JungleBrothers",
  author_email="junglebrothers@gmail.com",
  description="Python Crypter File FUD",
  long_description_content_type="text/markdown",
  url="https://github.com/junglebrothers",
  project_urls={
    "GitHub": "https://github.com/junglebrothers/",
  },
  license="MIT",
  keywords=["discord"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  packages=find_packages(),
  install_requires=['requests', 'sockets', 'pypiwin32', 'pycryptodome', 'uuid']
)