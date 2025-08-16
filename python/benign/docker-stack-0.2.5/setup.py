from setuptools import setup, find_packages

setup(
    name="docker-stack",
    version="0.2.5",
    description="CLI for deploying and managing Docker stacks.",
    long_description=open("README.md").read(),  # You can include a README file to describe your package
    long_description_content_type="text/markdown",
    author="Sudip Bhattarai",
    author_email="sudip@bhattarai.me",
    url="https://github.com/mesudip/docker-stack",  # Replace with your project URL
    packages=find_packages(),
    install_requires=[
        "PyYAML"
    ],
    entry_points={
        "console_scripts": [
            "docker-stack=docker_stack.cli:main",  # The function main() inside docker_stack.cli module
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
