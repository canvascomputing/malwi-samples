import setuptools
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="qt5-cef",
    version="1.1.13",
    author="Burgeon Developer",
    author_email="huai.y@burgeon.cn",
    description="A simple tool kit for create desktop application",
    url="https://gitee.com/hycool/qt5_cef.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    include_package_data=True,
    package_data={
        '': ['*.js'],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
    # install_requires=['PyQt5==5.11.2', 'cefpython3==57.1', 'pywin32==223'],
)
