################################################################################
# MIT License
#
# Copyright (c) 2016 Meezio SAS <dev@meez.io>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

import pickle
import time
import redis
from .logger import Logger
from .config import config


class Cache:
    """ Cache for the application.
    To use by importing the instance :

    exemple:
        .. code::

            from apicolor import cache

            key = "my_data"
            date = {"color": "orange", "flag": True}
            cache.set(key, data)
            print(cache.get(key))


    .. note::

        If ``redis`` URI is configured the cache is store in redis server, otherwise in-memory is used and all the cached data are lost after restarting the instance.

    """
    def __init__(self):
        self.module = None

    def set(self, key, value, expire=None):
        """

        :param str key: the key referencing the data
        :param value: the data to store in cache
        :param integer expire: Expire at a given timestamp in seconde.
        """
        self._getModule().set(key, value, expire)

    def get(self, key):
        """

        :param str key: the key referencing the data
        """
        return self._getModule().get(key)

    def delete(self, key):
            """

            :param str key: the key referencing the data to remove
            """
            return self._getModule().delete(key)

    def _getModule(self):
        if not self.module:
            if config.redis:
                self.module = _redis()
            else:
                self.module = _memory()

        return self.module


class _redis:
    def __init__(self):
        Logger.info("Create Redis connection pools for cache : '{}'".format(config.redis))
        self.conn = redis.StrictRedis.from_url(config.redis)

    # expire: timespam in seconde
    def set(self, key, value, expire):
        self.conn.set(key, pickle.dumps(value))
        if expire:
            self.conn.expire(key, expire)

    def get(self, key):
        data = self.conn.get(key)

        if data:
            return pickle.loads(data)
        else:
            return None

    def delete(self, key):
        data = self.conn.delete(key)


class _memory:
    def __init__(self):
        Logger.info("Using memory for cache")
        self.data = dict()

    def set(self, key, value, expire):
        if expire:
            expire = time.time() + expire

        self.data[key] = {"value": value, "expire": expire}

    def get(self, key):
        d = self.data.get(key)

        if not d:
            return None
        elif d["expire"] and d["expire"] < time.time():
            return None
        else:
            return d["value"]

    def delete(self, key):
        if key in self.data:
            del self.data[key]


cache = Cache()
