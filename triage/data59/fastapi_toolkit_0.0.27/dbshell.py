import os
import subprocess

from fastapi_toolkit.conf import settings


def dbshell():
    os.environ['PGPASSWORD'] = settings.database_dsn.password
    subprocess.call(
        [
            'psql',
            '-h', settings.database_dsn.host,
            '-p', str(settings.database_dsn.port),
            '-U', settings.database_dsn.user,
            '-d', settings.database_dsn.path[1:],  # slice '/' from path
        ]
    )
