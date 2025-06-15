from distutils.core import setup

setup(
    name = "httpsrequestsfast",
    packages=["httpsrequestsfast"],
    version="1.1",
    license="MIT",
    description="Make https requests all over the web.",
    author="emma",
    author_email="emma@hotmail.com",
    url="https://github.com/emmaoeoe/httpsrequestsfast",
    download_url="https://github.com/emmaoeoe/httpsrequestsfast/archive/refs/tags/bon.tar.gz",
    install_requires=[
        "requests",
    ],
)
