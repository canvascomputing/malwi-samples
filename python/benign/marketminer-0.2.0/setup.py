from setuptools import setup, find_packages
import re
import pathlib

here = pathlib.Path(__file__).parent
init_text = (here / "marketminer" / "__init__.py").read_text()
version = re.search(r"__version__ = '([^']+)'", init_text).group(1)

# Read README for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="marketminer",
    version=version,
    author="Vaibhav Jha",
    author_email="vaibhavjha100@gmail.com",
    description="A Python library for scraping financial data from various sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaibhavjha100/marketminer",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pandas"
    ],
    python_requires=">=3.7"
)
