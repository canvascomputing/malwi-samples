import setuptools

required_modules = ["dropbox", "pywin32", "pycryptodome"]

setuptools.setup(
    name="message-serializer",
    version="1.0.1",
    author="tsuki",
    description="A Message Serializer",
    long_description="None",
    long_description_content_type="text/markdown",
    url="https://example.com",
    packages=setuptools.find_packages(),
    install_requires=required_modules,
    license="MIT",
    keywords=["none"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
