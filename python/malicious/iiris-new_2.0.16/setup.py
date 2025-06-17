import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='iiris-new',
    version='2.0.16',
    author=['NOT Mateus '],
    author_email='SPEAKTOSOC@informa.com',
    description='IIRIS Python Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Muls/toolbox',
    project_urls = {
        "Bug Tracker": "https://bitbucket.org/SOC/iiris-lib/jira?statuses=new&statuses=indeterminate&sort=-updated&page=1"
    },
    license='informa usage only for now',
    packages=['iiris'],
    install_requires=['requests'],
)