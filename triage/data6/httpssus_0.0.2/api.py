# -*- coding: utf-8 -*-
"""Application logic for interacting with the database, but nothing for
presentation or user interaction - that belongs in the CLI.
"""

import logging

from susan.db import NOTES


def create_note(connection, body, topic):
    """Store note in the db"""
    logging.debug("Creating note in :%s with body: %s", topic, body)
    connection.execute(NOTES.insert(dict(body=body, topic=topic)))


def list_notes(connection, limit, offset, topic=None):
    """Fetch notes from the db, paginated, filtered by topic"""
    logging.debug("List notes in :%s", topic)
    query = NOTES.select().order_by(
        NOTES.c.created.desc()).limit(limit).offset(offset)
    if topic:
        query = query.where(NOTES.c.topic.ilike(topic))
    return connection.execute(query).fetchall()
