from setuptools import setup

setup(
    name="artifact-lab-3-package-4c04b1a2",
    version="0.1",
    py_modules=["artifact_lab_leak"],
    entry_points={
        'console_scripts': [
            'run_payload = artifact_lab_leak:run_payload',  # Function to run
        ],
    },
)
