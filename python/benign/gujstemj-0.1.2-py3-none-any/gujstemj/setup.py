# setup.py

from setuptools import setup, find_packages

setup(
    # Name, version, description, authors, etc. are defined in pyproject.toml
    # and will be picked up from there. Do NOT duplicate them here.
    packages=find_packages(),

    # --- License Declaration ---
    # This is the string that appears in the 'License:' field in METADATA
    license='MIT License', # Important: This exact string, or "MIT"

    # This tells setuptools to include the specified files as license files in the package.
    # It might create the 'license_files' metadata field if needed by setuptools.
    license_files=['LICENSE'], # Path to your license file(s)

    # Classifiers should ideally be in pyproject.toml
    # Do NOT include them here unless there's a specific reason or conflict.
)