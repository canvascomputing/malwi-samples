from setuptools import setup, find_packages

setup(
    name="artifact_lab_3_package_24ddbc49",  # Your package name
    version="0.2.0",  # Initial version
    author="Your Mum",
    author_email="your_email@example.com",
    description="Leaking environment variables via HTTP requests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["flag"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
