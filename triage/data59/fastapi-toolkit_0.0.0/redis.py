import logging
from contextlib import asynccontextmanager
from typing import ContextManager

import aioredis

from fastapi_toolkit.conf import settings

__all__ = (
    'get_redis_pool',
    'create_redis_pool',
    'close_redis_pool',
    'redis_connection_pool'
)

logger = logging.getLogger(settings.project)
_redis_pool: aioredis.ConnectionPool = None  # noqa


def get_redis_pool() -> aioredis.ConnectionPool:
    if _redis_pool is None:
        raise ValueError(
            'Redis pool is undefined. '
            'You need to call `createredis_pool` first.'
        )
    return _redis_pool


async def create_redis_pool() -> aioredis.ConnectionPool:
    global _redis_pool
    await close_redis_pool()
    if settings.redis_dsn:
        _redis_pool = aioredis.ConnectionPool.from_url(
            settings.redis_dsn,
            max_connections=settings.redis_max_connections
        )
    else:
        logger.warning('Can not create redis pool. Redis dsn is not defined.')
    return _redis_pool


async def close_redis_pool():
    global _redis_pool
    if _redis_pool is not None:
        await _redis_pool.disconnect()


@asynccontextmanager
async def redis_connection_pool() -> ContextManager[aioredis.Redis]:
    try:
        yield aioredis.Redis(connection_pool=get_redis_pool())
    finally:
        pass
