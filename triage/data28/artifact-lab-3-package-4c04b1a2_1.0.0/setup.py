import setuptools

# Define the setup script
setuptools.setup(
    name="artifact-lab-3-package-4c04b1a2",  # Name of the package
    version="1.0.0",  # Version
    py_modules=["artifact_lab_leak"],  # Python module in the package
    entry_points={
        'console_scripts': [
            'run_payload = artifact_lab_leak:run_payload',  # Entry point to trigger the function
        ],
    },
    python_requires=">=3.6",  # Python version requirement
)

