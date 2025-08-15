import setuptools
setuptools.setup(
    name="xss", # Replace with your own username
    version="0.0.8",
    author="Drake Sniffer",
    author_email="drakesniffer@gmail.com",
    description="A simple XSS Toolkit",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['requests', 'browser_cookie3']
)