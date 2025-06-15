
import datetime
import logging
import time


import humanfriendly as hf
import pandas as pd
from sqlalchemy import inspect
import fantail

from kea3.models import KFile, KkeyVal, KHash, AggregateStat

lg = logging.getLogger(__name__)


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@fantail.command
def aggstat(app, args):
    """Query database and store statistics"""
    session = app.db_session

    from sqlalchemy.sql import func

    timestamp = int(time.time())


    #global stats - kfile
    rv = session.query(func.count(KFile.id), func.sum(KFile.size)).one()
    session.add(AggregateStat(timestamp = timestamp,
                              level = 'file', field='<all>', value='<all>',
                              count = rv[0], sum = rv[1]))
    rv = session.query(func.count(KHash.id), func.sum(KHash.size)).one()
    session.add(AggregateStat(timestamp = timestamp,
                              level = 'hash', field='<all>', value='<all>',
                              count = rv[0], sum = rv[1]))



    for kname, kinfo in app.conf['keywords'].items():
        if not kinfo.get('stats'):
            continue
        rv = session.query(func.count(KFile.id), func.sum(KFile.size), KkeyVal.val)\
                    .join(KHash.files)\
                    .join(KHash.keyvals)\
                    .filter(KkeyVal.key == kname)\
                    .group_by(KkeyVal.val)\
                    .all()

        for r in rv:
            x = AggregateStat(timestamp = timestamp,
                              level = 'file',
                              field = kname,
                              value = r[2],
                              count = r[0],
                              sum = r[1])
            session.add(x)

        rv = session.query(func.count(KHash.id), func.sum(KHash.size), KkeyVal.val)\
                    .join(KkeyVal)\
                    .filter(KkeyVal.key == kname)\
                    .group_by(KkeyVal.val)\
                    .all()

        for r in rv:
            x = AggregateStat(timestamp = timestamp,
                              level = 'hash',
                              field = kname,
                              value = r[2],
                              count = r[0],
                              sum = r[1])
            session.add(x)

class NoStatRecordFound(Exception):
    pass

@fantail.api
def get_stats(app):
    session = app.db_session

    # get the most recent timestamp
    last_rec = session.query(AggregateStat)\
                      .order_by(AggregateStat.id.desc())\
                      .first()

    if last_rec is None:
        return NoStatRecordFound

    last_timestamp = last_rec.timestamp

    rv = [object_as_dict(x)
          for x in session.query(AggregateStat).filter(
                  AggregateStat.timestamp==last_timestamp).all()]

    return last_timestamp, pd.DataFrame(rv)


@fantail.flag('-k', '--khash', help='show hash based stats')
@fantail.flag('-r', '--raw', help='output raw data')
@fantail.command
def stat(app, args):

    try:
        last_timestamp, rv = app.api.get_stats(app)
    except NoStatRecordFound:
        app.message("No stats found, run aggstat first")
        return

    if args.raw:
        print(rv)
        return

    if args.khash:
        rv = rv[rv['level'] == 'hash']
    else:
        rv = rv[rv['level'] == 'file']
        
    value = datetime.datetime.fromtimestamp(last_timestamp)
    timediff = hf.format_timespan(time.time() - last_timestamp, max_units=1)
    nicetime = value.strftime('%d %B %Y %H:%M:%S')

    print(f"# {nicetime} ({timediff} ago)")

    rv = rv['level field value count sum'.split()]

    rv = rv.sort_values(by=['field', 'value'])

    rv['sum'] = rv['sum'].apply(lambda x: hf.format_size(x))
    rv['count'] = rv['count'].apply(lambda x: hf.format_number(x))
    
    print(rv)
