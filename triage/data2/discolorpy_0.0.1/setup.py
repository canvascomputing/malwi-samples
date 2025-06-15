import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discolorpy",
    version="0.0.1",
    author="Juif1337",
    author_email="grostuturdemerde@proton.me",
    description="module for beautiful color in discord tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoldenShowers667/pydiscolor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)