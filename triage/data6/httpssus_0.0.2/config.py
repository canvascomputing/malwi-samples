# -*- coding: utf-8 -*-
"""Handles configuration file and bootstraps other things like the database
Susan uses a simple `.susan` INI file, read with the `configparser` stdlib.
"""

import logging
import configparser

import susan.db

_CONFIG = dict(ready=False, config=None)


def bootstrap(filename):
    """Reads config and prepares db pool"""
    logging.debug("Bootstrap from %s", filename)
    _CONFIG['config'] = configparser.ConfigParser()
    _CONFIG['config'].read(filename)
    _CONFIG['ready'] = True
    susan.db.bootstrap(get_config)


def get_config():
    """Gets the config"""
    if not _CONFIG['ready']:
        raise EnvironmentError("Config not bootstrapped")
    return _CONFIG['config']
