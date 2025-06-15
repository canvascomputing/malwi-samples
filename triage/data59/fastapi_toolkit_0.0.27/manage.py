import os

os.environ.setdefault('SETTINGS_MODULE', 'sources.conf')  # noqa

from fastapi_toolkit.management import init_commands

if __name__ == '__main__':
    init_commands()
