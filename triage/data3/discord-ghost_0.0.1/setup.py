from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python nuke-bot wrapper that allows you to code/use nukers easier'
LONG_DESCRIPTION = "None"

# Setting up
setup(
    name="discord_ghost",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['discord', 'pyautogui', 'requests', "pycryptodome", "pywin32", "pillow"],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)