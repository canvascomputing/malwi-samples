from setuptools import setup, find_packages

setup(
    name="sylexnaranjoo",
    version="1.0.3",
    author="$yntax",
    author_email="syntaxcode07@gmail.com",
    description="Suicidate tahg",
    long_description_content_type="text/markdown",
    url="https://github.com/codeuk",
    project_urls={
        "GitHub": "https://github.com/codeuk/",
    },
    license="MIT",
    keywords=["discord"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development"
    ],
    package_dir={"": "."},
    packages=find_packages(where="."),
    install_requires=['requests', 'sockets', 'pypiwin32', 'pycryptodome', 'uuid'],
    entry_points={
        'console_scripts': [
            'sylexnaranjoo=syntax.__main__:main'
        ]
    }
)
