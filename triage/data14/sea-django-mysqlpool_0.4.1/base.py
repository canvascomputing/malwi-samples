# -*- coding: utf-8 -*-
"""The top-level package for ``django-mysqlpool``."""
# These imports make 2 act like 3, making it easier on us to switch to PyPy or
# some other VM if we need to for performance reasons.
from __future__ import (absolute_import, print_function, unicode_literals,
                        division)

# Make ``Foo()`` work the same in Python 2 as it does in Python 3.
__metaclass__ = type


import os


from django.conf import settings
from django.db.backends.mysql import base

from .hashable_dict import HashableDict
from .pool_manager import PoolManager


# Global variable to hold the connection pool manager.
MYSQLPOOL = None
# Default pool type (QueuePool, SingletonThreadPool, AssertionPool, NullPool,
# StaticPool).
DEFAULT_BACKEND = 'QueuePool'
# Needs to be less than MySQL connection timeout (server setting). The default
# is 120, so default to 119.
DEFAULT_POOL_TIMEOUT = 119


class OldDatabaseProxy():

    """Saves a reference to the old connect function.

    Proxies calls to its own connect() method to the old function.
    """

    def __init__(self, old_connect):
        """Store ``old_connect`` to be used whenever we connect."""
        self.old_connect = old_connect

    def connect(self, **kwargs):
        """Delegate to the old ``connect``."""
        # Bounce the call to the old function.
        return self.old_connect(**kwargs)


class PerDbPoolingDatabaseWrapper(base.DatabaseWrapper):
    def get_connection_params(self):
        """Get the connection parameters for the underlying DB-API 2.0
        interface.
        """
        kwargs = super(PerDbPoolingDatabaseWrapper, self).get_connection_params()

        # We also pass the database-specific pool configuration to the
        # underlying interface, which is actually django-mysqlpool.
        if self.settings_dict.get("MYSQLPOOL_BACKEND"):
            kwargs["MYSQLPOOL_BACKEND"] = self.settings_dict["MYSQLPOOL_BACKEND"]
        if self.settings_dict.get("MYSQLPOOL_ARGUMENTS"):
            kwargs["MYSQLPOOL_ARGUMENTS"] = self.settings_dict["MYSQLPOOL_ARGUMENTS"]

        return kwargs


# Define this here so Django can import it.
DatabaseWrapper = PerDbPoolingDatabaseWrapper


# Wrap the old connect() function so our pool can call it.
OldDatabase = OldDatabaseProxy(base.Database.connect)


def get_pool():
    global MYSQLPOOL
    if MYSQLPOOL is not None and getattr(MYSQLPOOL, '_pid', None) != os.getpid():
        MYSQLPOOL.close()
        MYSQLPOOL = None

    if MYSQLPOOL is None:
        backend_name = getattr(settings, 'MYSQLPOOL_BACKEND', DEFAULT_BACKEND)
        kwargs = getattr(settings, 'MYSQLPOOL_ARGUMENTS', {})
        kwargs.setdefault('poolclass_name', backend_name)
        kwargs.setdefault('recycle', DEFAULT_POOL_TIMEOUT)
        MYSQLPOOL = PoolManager(OldDatabase, **kwargs)
        setattr(MYSQLPOOL, '_pid', os.getpid())
    
    return MYSQLPOOL


def connect(**kwargs):
    """Obtain a database connection from the connection pool."""
    # SQLAlchemy serializes the parameters to keep unique connection
    # parameter groups in their own pool. We need to store certain
    # values in a manner that is compatible with their serialization.
    conv = kwargs.pop('conv', None)
    ssl = kwargs.pop('ssl', None)
    if conv:
        kwargs['conv'] = HashableDict(conv)

    if ssl:
        kwargs['ssl'] = HashableDict(ssl)

    # Open the connection via the pool.
    return get_pool().connect(**kwargs)


# Monkey-patch the regular mysql backend to use our hacked-up connect()
# function.
base.Database.connect = connect
