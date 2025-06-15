from pydantic import AnyUrl

from fastapi_toolkit.conf.global_settings import GlobalSettings


class Settings(GlobalSettings):
    project: str = '{{cookiecutter.project_name}}'
    alembic_directory: str = 'sources/alembic'
    alembic_config: str = 'sources/alembic/alembic.ini'
    application = 'sources.main:app'
    use_https = False
    database_dsn: AnyUrl = 'postgresql+asyncpg://{{cookiecutter.database_user}}:{{cookiecutter.database_password}}@{{cookiecutter.database_host}}:{{cookiecutter.database_port}}/{{cookiecutter.database_name}}'  # noqa
