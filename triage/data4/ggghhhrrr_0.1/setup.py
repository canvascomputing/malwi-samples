from setuptools import setup, find_packages

setup(
    name="ggghhhrrr",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "ggghhhrrr=ggghhhrrr.__init__:notify",
        ],
    },
)
