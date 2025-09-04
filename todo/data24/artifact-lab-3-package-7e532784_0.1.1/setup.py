from setuptools import setup, find_packages
# If you have a README.md file that you want to use as your long description, you can include it like this:
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='artifact-lab-3-package-7e532784',  # The name of your package
    version='0.1.1',  # The version of your package
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[],  # Dependencies for your package (leave empty if none)

    # Additional metadata
    long_description=long_description,  # This will pull in your README.md file as the long description
    long_description_content_type="text/markdown",  # Specify the content type of long_description (e.g., text/markdown or text/x-rst)
)
