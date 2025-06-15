# Standard Library
import logging

# Third Party Library
import newrelic.agent
import sentry_sdk
from fastapi import FastAPI
from newrelic.agent import ASGIApplicationWrapper
from newrelic.api.transaction import current_transaction
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.httpx import HttpxIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from starlette.types import ASGIApp

from fastapi_toolkit.conf import settings


class NewRelicMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope, receive, send):
        transaction = current_transaction()
        if transaction:
            _method = scope.get('method', '')
            _path = scope.get('path', '/')
            transaction_name = f'{_method}: {_path}'
            newrelic.agent.set_transaction_name(transaction_name, 'Uri')
            transaction._name_priority = None
        return await self.app(scope, receive, send)


def init_newrelic(app: FastAPI, newrelic_ini_path):
    if settings.new_relic_enabled:
        newrelic.agent.initialize(
            newrelic_ini_path,
            environment=settings.environment
        )

        app.add_middleware(NewRelicMiddleware)
        app = ASGIApplicationWrapper(app)

    return app


def init_sentry(app):
    if settings.sentry_enabled and settings.sentry_dsn:
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            environment=settings.environment,
            integrations=[
                LoggingIntegration(
                    level=logging.INFO,
                    event_level=logging.WARNING
                ),
                SqlalchemyIntegration(),
                HttpxIntegration()
            ]
        )
        app.add_middleware(SentryAsgiMiddleware)
    return app
