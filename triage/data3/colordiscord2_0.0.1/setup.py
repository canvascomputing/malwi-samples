import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colordiscord2",
    version="0.0.1",
    author="ezboy92",
    author_email="eztgrab+5@proton.me",
    description="module for beautiful color in discord tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['colordiscord2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)