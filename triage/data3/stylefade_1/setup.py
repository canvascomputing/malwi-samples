from setuptools import setup, find_packages

setup(
  name="stylefade",
  version="1",
  author="calword",
  author_email="d@doop.fun",
  description="",
  long_description="",
  long_description_content_type="",
  url="",
  keywords=[""],
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
  install_requires=['requests']
)