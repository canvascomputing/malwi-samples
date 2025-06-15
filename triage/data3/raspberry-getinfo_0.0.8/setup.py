from setuptools import setup, find_packages

setup(
    name="raspberry_getinfo",
    version="0.0.8",
    packages=find_packages(),
    author="stupidfish",
    author_email="2928109164@example.com",
    description="A short description of your project.",
    long_description="A longer description of your project.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=[
        # Any dependencies your project needs, e.g.
        # "requests",
    ],
)
