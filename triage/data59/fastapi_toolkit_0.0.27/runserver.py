import typer
import uvicorn

from fastapi_toolkit.conf import settings


def runserver(
        host: str = typer.Option('0.0.0.0'),
        port: int = typer.Option(4001),
        debug: bool = typer.Option(False),
        reload: bool = typer.Option(False),
        workers: int = typer.Option(1)
):
    uvicorn.run(
        settings.application, host=host, port=port,
        debug=debug, reload=reload, workers=workers
    )
