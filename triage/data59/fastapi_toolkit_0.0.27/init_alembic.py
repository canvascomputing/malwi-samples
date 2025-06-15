import typer
from alembic.command import init
from alembic.config import Config

from fastapi_toolkit.conf import settings


def init_alembic(directory: str = typer.Option(None)):
    directory = directory or settings.alembic_directory
    init(Config(settings.alembic_config), directory)
