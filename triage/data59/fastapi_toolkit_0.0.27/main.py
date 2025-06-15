# Standard Library
import os  # isort:skip
os.environ.setdefault('SETTINGS_MODULE', 'sources.conf')  # noqa

from sources.api import api_router as v1_api_router

# Third Party Library
from fastapi_toolkit.application import app

app.include_router(v1_api_router, prefix='/v1')


def get_app():
    return app
