"""Setup script for the mqtt-connector package."""

from setuptools import find_packages, setup

setup(
    name="mqtt-connector",
    version="0.1.0",
    author="Alex Gonzalez",
    author_email="alex@muxu.io",
    description="A robust MQTT connector for asynchronous MQTT communication",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/muxu-io/mqtt-connector",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "paho-mqtt>=2.0.0",  # MQTT client library
        "asyncio-mqtt>=0.12.0",  # Async wrapper for paho-mqtt
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
    ],
    python_requires=">=3.7",
)
