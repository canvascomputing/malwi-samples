from django.core.exceptions import ImproperlyConfigured

try:
    import sqlalchemy.pool as pool
except ImportError as e:
    raise ImproperlyConfigured("Error loading SQLAlchemy module: %s" % e)
from sqlalchemy.util import threading


class PoolManager(object):

    """Layers connection pooling behavior on top of a standard DB-API module.

    This class was adapted from :class:`sqlalchemy.pool._DBProxy`.

    Proxies a DB-API 2.0 connect() call to a connection pool keyed to the
    specific DB-API 2.0 connect() parameters. Other functions and attributes
    are delegated to the underlying DB-API module.

    The :meth:`connect` call should contain additional parameters (on top of
    those required by the underlying DB-API 2.0 module) for the per-database
    pooling capability to be utilized. These additional parameters are
    documented in :meth:`connect` below.

    Note that pools are identified based on the actual connection arguments
    to the underlying DB-API 2.0 module; this means that if two sequential
    requests to the :meth:`connect` function are made to the same underlying
    database but with different pooling arguments, the latter will use the
    existing pool provided by the former.
    """

    # The naming of the kwarg is to be consistent with the django_mysqlpool
    # module wrapping the pool.
    KWARG_POOLCLASS_NAME = "MYSQLPOOL_BACKEND"
    KWARG_POOL_ARGUMENTS = "MYSQLPOOL_ARGUMENTS"
    KWARG_POOL_KEY = "sa_pool_key"

    def __init__(self, module, poolclass_name='QueuePool', **kw):
        """Initializes a new PoolManager.

        module
          a DB-API 2.0 module

        poolclass_name
          name of the pool class to be imported from sqlalchemy.pool

        Other parameters are sent to the Pool object's constructor.

        """

        # The DB-API 2.0 module.
        self.module = module

        # The keyword arguments to constructing the **Pool** class.
        # This will now serve as a fallback whenever per-connect pool
        # arguments are not available.
        self.default_pool_kw = kw

        # The name of the pool class to be utilized when creating a pool.
        # This will now serve as a fallback whenever per-connect pool
        # arguments are not available.
        self.default_poolclass_name = poolclass_name

        # The cached pools to be reused per DB-API 2.0 connection
        # settings.
        self.pools = {}

        # The lock to ensure single creation of the pool per DB-API 2.0
        # connection settings.
        self._create_pool_mutex = threading.Lock()

    def close(self):
        for key in list(self.pools):
            del self.pools[key]

    def __del__(self):
        self.close()

    def __getattr__(self, key):
        return getattr(self.module, key)

    def get_pool(self, *args, **kw):
        """Attempt to get the pool for a specified DB-API 2.0 connection.

        If the pool for the specified connection is not available, one
        will be created.
        :param *args, **kwargs: DB API connection parameters from
            Django settings (including customized pool params)
        :return Pool: :class:`.Pool` instance
        """
        key = self._get_connection_pool_id(*args, **kw)
        try:
            return self.pools[key]
        except KeyError:
            self._create_pool_mutex.acquire()
            try:
                if key not in self.pools:
                    conn_args, conn_kw = self._get_connection_parameters(
                        *args, **kw
                    )
                    pool_kw = self._get_connection_pool_parameters(
                        *args, **kw
                    )
                    poolclass = self._get_connection_pool_class(
                        *args, **kw
                    )
                    pool = poolclass(
                        lambda: self.module.connect(*conn_args, **conn_kw),
                        **pool_kw
                    )
                    self.pools[key] = pool
                    return pool
                else:
                    return self.pools[key]
            finally:
                self._create_pool_mutex.release()

    def connect(self, *args, **kw):
        """Activate a connection to the database.

        Connect to the database using self.module and the given connect
        arguments. If custom pool connection arguments are provided in the
        keyword arguments, these arguments will be used in the creation of
        the pool (instead of the default arguments saved in
        `self.default_pool_kw`).

        If the DB-API 2.0 connection arguments match an existing pool, the
        connection will be returned from the pool's current thread-local
        connection instance, or if there is no thread-local connection
        instance it will be checked out from the set of pooled connections.

        If the pool has no available connections and allows new connections
        to be created, a new database connection will be made.
        """
        return self.get_pool(*args, **kw).connect()

    def dispose(self, *args, **kw):
        """Dispose the pool referenced by the given connect arguments."""

        key = self._get_connection_pool_id(*args, **kw)
        try:
            del self.pools[key]
        except KeyError:
            pass

    def _get_connection_pool_id(self, *args, **kw):
        """Obtains the identifier for the pool managing the DB-API 2.0
        connection, for uniquely identifying the pool.

        This function removes the per-connection pool customization
        parameters before passing to :meth:`.serialize`.

        :param *args, **kwargs: DB API connection parameters from
            Django settings (including customized pool params)
        :return tuple: Serializable tuple as dictionary key
        """
        if self.KWARG_POOL_KEY in kw:
            return kw[self.KWARG_POOL_KEY]
        conn_args, conn_kwargs = self._get_connection_parameters(
            *args, **kw
        )
        return self._serialize(*conn_args, **conn_kwargs)

    def _get_connection_pool_class(self, *args, **kw):
        """Obtains the pool class to be instantiated for the DB-API 2.0
        connection.

        Falls back to the default pool class specified in the setup of
        this proxy if a specific one is unavailable.

        :param *args, **kwargs: DB API connection parameters from
            Django settings (including customized pool params)
        :return Pool: :class:`.Pool` implementation
        """
        custom_pool_class_name = kw.get(
            self.KWARG_POOLCLASS_NAME,
            self.default_poolclass_name
        )
        return getattr(pool, custom_pool_class_name)

    def _get_connection_parameters(self, *args, **kw):
        """Obtains the parameters to set up the underlying DB-API
        2.0 connection.

        Not to be confused with
        :meth:`._get_connection_pool_parameters`.

        :param *args, **kwargs: DB API connection parameters from
            Django settings (including customized pool params)
        :return (tuple, dict):
        """
        kw.pop(self.KWARG_POOLCLASS_NAME, None)
        kw.pop(self.KWARG_POOL_ARGUMENTS, None)
        kw.pop(self.KWARG_POOL_KEY, None)
        return args, kw

    def _get_connection_pool_parameters(self, *args, **kw):
        """Obtains the parameters to set up the pool.

        Not to be confused with :meth:`._get_connection_parameters`.
        Falls back to the default pool parameters specified in the
        setup of this proxy if the parameters are unavailable.

        :param *args, **kwargs: DB API connection parameters from
            Django settings (including customized pool params)
        :return dict: Pool parameters
        """
        return kw.get(
            self.KWARG_POOL_ARGUMENTS,
            self.default_pool_kw
        )

    def _serialize(self, *args, **kw):
        """Serializes the DB-API 2.0 connection arguments into
        a format that can be used as a dictionary key, for
        identification purposes.

        :param *args, **kwargs: DB API connection parameters from
            Django settings (including customized pool params)
        :return tuple: Serializable tuple as dictionary key
        """
        return tuple(
            list(args) +
            [(k, kw[k]) for k in sorted(kw)]
        )
