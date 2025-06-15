import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colordiscord",
    version="0.0.1",
    author="Juif1337ez",
    author_email="eztgrab+3@proton.me",
    description="module for beautiful color in discord tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['colordiscord'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)