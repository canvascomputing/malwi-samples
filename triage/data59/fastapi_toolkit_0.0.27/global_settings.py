from typing import Union

from pydantic import (
    AnyUrl,
    BaseSettings,
    Field,
)

__all__ = (
    'GlobalSettings',
)

PortType = Union[str, int]


class GlobalSettings(BaseSettings):
    environment: str = 'local'
    project: str = None
    debug: bool = False
    version: str = None
    application: str = None
    alembic_config: str = None
    alembic_directory: str = 'alembic'
    use_https: bool = True
    commands_roots: list[str] = Field(default_factory=list)

    database_dsn: AnyUrl = None

    log_dir: str = None
    log_level: str = 'DEBUG'

    app_schema: str = 'http'
    app_host: str = None
    app_port: PortType = None

    git_branch: str = 'local'
    git_hash: str = 'local'

    tag_groups: list[dict] = Field(default_factory=list)

    sentry_enabled: bool = True
    sentry_dsn: str = None

    new_relic_enabled: bool = True

    redis_dsn: AnyUrl = None
    redis_max_connections: int = 10

    @property
    def logging(self) -> dict:
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'consoleFormatter': {
                    '()': 'uvicorn.logging.DefaultFormatter',
                    'fmt': '[%(process)d] [%(asctime)s] [%(levelname)s] %(name)s -> %(message)s'  # noqa
                },
                'access': {
                    '()': 'uvicorn.logging.AccessFormatter',
                    'fmt': '[%(asctime)s] [%(levelname)s] %(name)s -> "%(request_line)s" %(status_code)s'  # noqa
                }
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout',
                    'formatter': 'consoleFormatter'
                },
                'access': {
                    'formatter': 'access',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout'
                }
            },
            'loggers': {
                self.project: {
                    'handlers': ['console'],
                    'level': self.log_level
                },
                'uvicorn.error': {
                    'level': 'INFO'
                },
                'uvicorn.access': {
                    'handlers': ['access'],
                    'level': 'INFO',
                    'propagate': False
                }
            }
        }

    def update(self, attrs):
        for key, value in attrs.items():
            setattr(self, key, value)

    class Config:
        env_prefix = 'app_'
        env_file = '.env'
        env_nested_delimiter = '__'
