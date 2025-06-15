# -*- coding: utf-8 -*-
"""SQLalchemy metadata and the db connection
Susan uses SQLite3 and stores this in a place from the config file
"""

import logging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, DateTime

SESSIONMAKER = sessionmaker()
BASE = declarative_base()
METADATA = MetaData()

NOTES = Table(
    "note",
    METADATA,
    Column('note_id', Integer, primary_key=True),
    Column('topic', String),
    Column('body', String),
    Column('created', DateTime(timezone=True), server_default=func.now()), )


def bootstrap(get_config):
    """Prepare the engine, fetch connection strings.
    Only run after config bootstrapping.
    If using SQLite3, this creates the db too.
    """
    connection_string = get_config().get('database', 'connection')
    logging.debug("Connection string: %s", connection_string)
    engine = create_engine(connection_string)
    METADATA.create_all(engine)
    SESSIONMAKER.configure(bind=engine)
