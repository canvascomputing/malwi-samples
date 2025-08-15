import setuptools
import importantpackage

setuptools.setup(
    name="importantpackage",
    version="0.1.30",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description="Very long description",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
    packages=setuptools.find_packages(),
)
