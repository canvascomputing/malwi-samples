"""Entry point for Susan command-line interface using `Click` library.
Presentation and user interaction happens here, but no db access.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from susan.config import bootstrap, get_config
from susan import api
from susan.db import SESSIONMAKER

import click
import pyperclip

DEFAULT_TOPIC = 'scratch'


@click.group()
@click.option('--debug/--no-debug', default=True)
def cli(debug):
    """Susan is a very simple note taker and implicit personal wiki
    """
    config_path = os.path.join(
        click.get_app_dir('susan', 'config.ini', force_posix=True))
    bootstrap(filename=config_path)
    log_filename = get_config().get('logging', 'filename')
    logging.basicConfig(filename=log_filename, level=logging.DEBUG)
    if debug:
        logging.debug('Debug mode')


@cli.command()
def version():
    """Get the version"""
    click.echo('Version: ')


@cli.command()
@click.option("--topic", "-t", default=None, help="topic name")
@click.option("--clipboard", "-p", is_flag=True, help="paste from clipboard")
@click.argument("body", required=False)
def note(body, topic, **kwargs):
    """Store a note in a topic
    """
    session = SESSIONMAKER()
    if kwargs['clipboard']:
        body = pyperclip.paste()
    if not body:
        body = click.edit()
    if not body:
        return
    if not topic:
        topic = DEFAULT_TOPIC
    api.create_note(session, body, topic=topic)
    session.commit()


@cli.command()
@click.option("--count", "-n", default=5, help="number of rows")
@click.option("--only-1", "-1", is_flag=True, help="only one row")
@click.option('--all-topics', is_flag=True)
@click.option("--clipboard", "-p", is_flag=True, help="copy to clipboard")
@click.argument("topic", required=False)
def head(topic,**kwargs):
    """Get the latest n notes in a topic
    """
    session = SESSIONMAKER()
    if not topic:
        topic = DEFAULT_TOPIC
    if kwargs['all_topics']:
        topic = None
    notes = api.list_notes(
        session, limit=1 if kwargs['only_1'] else kwargs['count'], offset=0, topic=topic)
    session.commit()
    for item in notes:
        click.echo(item.body)
    if kwargs['clipboard']:
        pyperclip.copy("\n".join([_.body for _ in notes]))
