import typer
from alembic.command import (
    downgrade,
    upgrade,
)
from alembic.config import Config

from fastapi_toolkit.conf import settings


def migrate(
        revision: str = typer.Option('head'),
        down: bool = typer.Option(False)
):
    alembic_config = Config(settings.alembic_config)
    method = downgrade if down else upgrade
    method(alembic_config, revision)
