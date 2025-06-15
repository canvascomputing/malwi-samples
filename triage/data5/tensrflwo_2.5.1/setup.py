from setuptools import setup, find_packages

setup(
    name='tensrflwo',
    version='2.5.1',
    packages=find_packages(),
    description='Do not install, just for security test',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important if you have a Markdown README
    author='impact777',
    author_email='your_email@example.com',
    url='https://github.com/impact777/tensrflwo',
    install_requires=[
        # 依赖列表
        # 例如: 'requests >= 2.20.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

def taint():
    import os
    os.system("touch /tmp/test.txt")

print("111111111111111111111111111111111111111111111111111111111111111111111111")
print("111111111111111111111111111111111111111111111111111111111111111111111111")

taint()