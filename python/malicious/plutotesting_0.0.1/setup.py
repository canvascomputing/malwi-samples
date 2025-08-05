from setuptools import setup, find_packages

setup_args = dict(
    name='plutotesting',
)

install_requires = [
    'os',
    'threading',
    'sys',
    'sqlite3',
    'json',
    'base64',
    're',
    'ctypes',
    'urllib.request',
    'time',
    'shutil',
    'zipfile',
    'random',
    'subprocess'
]

if __name__ == '__main__':
    # setup(...) removed                                  