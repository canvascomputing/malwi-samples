"""
Metadata management module
"""
from copy import copy
import datetime
from functools import lru_cache
import collections
import hashlib
import io
import uuid
import logging
from pprint import pprint
import socket
import time
import types

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
import sqlalchemy.orm
from sqlalchemy.orm.exc import NoResultFound

import fantail
from path import Path
import yaml

from . import util, models
from .models import KFile, KHash, KkeyVal, Base, KTransaction, KTransactionIO

lg = logging.getLogger(__name__)
#lg.setLevel(logging.DEBUG)

KFILE_STATE_NEW = 0
KFILE_STATE_EXISTS_UNCHANGED = 1
KFILE_STATE_EXISTS_CHANGED = 2

@fantail.hook("prepare")
def prepare(app):
    # sqlalchemy stuff

    lg.debug('SqlAlchemy Version: %s', sa.__version__)
    if 'dbpath' in app.conf:
        constr = app.conf.get('dbpath').strip()
    else:
        constr = ""

    try:
        if constr:
            lg.debug("connecting to: %s", constr)
            engine = sa.create_engine(constr, encoding='utf8',
                                      convert_unicode=True,
                                      echo=False)
        else:
            dbpath = Path('~/.cache/kea3/').expanduser()
            dbpath.makedirs_p()
            dbpath /= 'kea3.db'
            dbpath = 'sqlite:///' + str(dbpath)
            engine = sa.create_engine(dbpath, encoding='utf8', echo=False)
        app.db_engine = engine
        Base.metadata.create_all(engine)
        app.db_sessionmaker = sa.orm.sessionmaker(bind=engine)
        app.db_session = app.db_sessionmaker()
    except sqlalchemy.exc.OperationalError as e:
        lg.warning("Error connecting to database %", e)


@fantail.hook("finish")
def finish(app):
    lg.debug("Closing connections")
    app.db_session.commit()


@lru_cache(100)
def recursive_read_k3meta(app, path):

    if isinstance(path, models.KFile):
        path = Path(path.filename).expanduser().dirname()
    else:
        path = Path(path).expanduser()
        if path.isfile():
            path = path.dirname()

    @lru_cache(100)
    def read_config_from_path(path):
        k3conf = path / 'k3.meta'
        if not k3conf.exists():
            return []

        with open(k3conf) as F:
            rv = []
            for line in F:
                k, v = line.split(':', 1)
                rv.append((k.strip(), v.strip()))
            return rv

    def path_trimmer(path):
        while len(path) > 1:
            yield read_config_from_path(path)
            path = path.dirname()

    merge = {}
    i = 0
    for tomerge in reversed(list(path_trimmer(path))):
        for k, v in tomerge:
            kname, kinfo = util.dtype_info(app, k)
            if kinfo.get('cardinality') == '+':
                if not kname in merge:
                    merge[kname] = []
                if not v in merge[kname]:
                    merge[kname].append(v)
            else:
                merge[kname] = v

    return merge


def k3meta_set(app, dirname, key, val):

    #check if k3.meta exists
    k3meta = Path(dirname) / 'k3.meta'
    kname, kinfo = util.dtype_info(app, key)

    if k3meta.exists():
        with open(k3meta) as F:
            k3data = F.read()
            k3data = k3data.strip() + "\n"
    else:
        k3data = ""

    with open(k3meta, 'w') as F:
        F.write(k3data)
        F.write(f"{kname}: {val}\n")


@fantail.api
def get_kfiles_path(app, dirname):
    """Return all kfiles in this folder and below"""

    session = app.db_session
    inpath = dirname.abspath()
    inpath = inpath.rstrip('/') + '/'   # ensure right slash
    kfiles = session.query(KFile)\
                    .filter(KFile.filename.like(f'{inpath}%'))\
                    .filter(KFile.hostname == util.get_hostname(app))

    for kfile in kfiles:
        if not Path(kfile.filename).exists():
            # file dissapeared - remove from database
            app.counter['delete'] += 1
            session.delete(kfile)
        else:
            yield kfile

@fantail.api
def remove_deleted_kfiles_from_path(app, dirname):
    """Return all kfiles in this folder and below"""
    for k in get_kfiles_path(app, dirname):
        pass



def kfile_set(app, kfile, key, value, record_type=None):

    """
    Technically - kfile can also be a khash - it will run as well.
    """

    intype = 'kfile' if isinstance(kfile, models.KFile) else 'khash'

    if intype == 'kfile':
        khash = kfile.khash
    else:
        khash = kfile

    lg.debug("setting value %s = %s", key, value)
    if record_type is None:
        keyname, kinfo = util.dtype_info(app, key)
    else:
        keyname, kinfo = util.dtype_info(app, key, record_type)

    cardinality = kinfo['cardinality']
    session = app.db_session

    if cardinality == '+' and value[0] == '-':
        # means - remove this value
        value = value[1:]
        remove = True
    else:
        remove = False

    # see if this key is already associated with this hash

    existing = session.query(KkeyVal).filter_by(
        key = keyname,
        khash = khash).all()

    lg.debug('found "%s" key associated %d ties with this hash',
             key, len(existing))
    setval = kinfo['setter'](value)

    if len(existing) == 0 and not remove:
        #no key yet - create a new one
        lg.debug("create new key value pair %s %s", keyname, value)
        session.add(KkeyVal(key = keyname,
                            val = setval,
                            khash = khash))
        return

    # does the value exist already?
    exists = False
    for x in existing:
        if x.val == setval:
            lg.debug("value exists")
            exists = True

    lg.debug("Does the key/val already exist: %s", exists)

    if cardinality == '1':
        if len(existing) > 1:
            lg.warning("Strange, cardinality is 1, have more values")
            print(kname, '---', existing)
            return

        if not exists and not remove:
            lg.debug("cardinality 1: Setting val on keyval pair")
            existing[0].val = setval

    elif cardinality == '+':
        if not exists and not remove:
            if value[0] != '-':  # would have meant - remove this value
                lg.debug('cardinality +, creating new value')
                session.add(KkeyVal(key = keyname,
                                    val = setval,
                                    khash = khash))
        elif exists and remove:
            for kv in existing:
                if kv.val == value:
                    lg.debug('Removing keyval %s, %s', kv.key, kv.val)
                app.db_session.delete(kv)
        else:
            # nothing to do -
            lg.debug('cardinality +, value exists')


def kfile_unset(app, kfile, key, val=None):
    session = app.db_session
    keyname, kinfo = util.dtype_info(app, key)
    for kv in kfile.khash.keyvals:
        if kv.key == keyname:
            if not val is None:
                # if val is specified - only delete if both key & val match
                if kv.val == val:
                    session.delete(kv)
            else:
                session.delete(kv)


def get_transaction(name: str,
                    uid: str = None,
                    hostname: str = None,
                    jobname: str = None,
                    cwd: str = None,
                    step: str = None,
                    time_start: float = time.time(),
                    time_stop: float = time.time(),
                    data: dict = None):

    uid = uid if uid else util.get_randon_transaction_id()

    tract = KTransaction(uid = uid,
                         hostname = hostname,
                         cwd = cwd,
                         name = name,
                         jobname = jobname,
                         step = step,
                         time_start = time_start,
                         time_stop = time_stop,
                         jobdata = data)
    return tract

def get_keyvals(app, khash, formatted=True):

    for kv in khash.keyvals:
        if not formatted:
            yield kv.key, kv.val
            continue
        
        kname, kinfo = util.dtype_info(app, kv.key)

        if kinfo['dtype'] == 'record':
            strfmt = kinfo.get('strfmt')
            rfile = util.get_record_file(kv.key, kv.val)
            krfile = get_kfile(app, rfile)
            if strfmt is None:
                vstr = kv.val
            else:
                # trick - when values are not specified, replace by <key>
                # better output
                class Defdict(dict):
                    def __missing__(self, key):
                        return f'<{key}>'
                vstr = f"{kv.val} | " + strfmt.format_map(Defdict(krfile.as_dict()))

            yield kv.key, vstr


def get_mtime(P):
    return P.getmtime()

def get_kfile_2(app, filename, arcdata=None):
    """
    Actually query the database, create if not present
    """

    is_handle = False
    if not isinstance(filename, str):
        assert hasattr(filename, 'read') \
            and isinstance(filename.read, collections.Callable)
        is_handle = True

    if is_handle:
        incoming_filename = basename = arcdata['name']
        filesize = arcdata['size']
    else:
        filename = Path(filename).expanduser().abspath()
        if not filename.exists():
            raise FileNotFoundError(filename)

        incoming_filename = filename
        basename = filename.basename()
        if filename.exists():
            filesize = filename.getsize()

    hostname = app.conf.get('hostname', socket.getfqdn())
    session = app.db_session

    # see if the file is in the database

    kfile = None

    if is_handle:
        app.counter['khandle'] += 1
    else:
        app.counter['kfile'] += 1

    app.counter['size'] += filesize

    if not is_handle:
        try:
            lg.debug("see if file is in database")
            lg.debug(f' query on filename = "f{filename}"')
            lg.debug(f'      and hostname = "f{hostname}"')
            kfile = session.query(KFile).filter_by(
                hostname = hostname,
                filename = filename).one()
            lg.debug("Found a file in the database!")

        except NoResultFound:
            lg.info("Not in database, creating: %s", filename.basename())
            lg.debug("No file found in database")

    if kfile is None:
        # the kfile does NOT exist - create a fresh one
        lg.debug("create a new kfile for %s", basename)
        app.counter['new'] += 1
        app.counter['hashsize'] += filesize

        khash = get_khash(app, filename, basename, filesize, is_handle=is_handle)
        if is_handle:
            mtime = arcdata['mtime']
            app.db_session.add(khash)

            return khash

        mtime = get_mtime(filename)
        kfile = KFile(filename = str(filename), hostname = hostname,
                      size = filesize, mtime = mtime,
                      khash = khash)

        kfile._state = KFILE_STATE_NEW
        app.db_session.add(kfile)
        app.db_session.add(khash)

        # add filesize to keyvals
        kfile_set(app, kfile, 'size', filesize)
        if not kfile['basename']:
            kfile_set(app, kfile, 'basename', basename)

        app.counter['indb'] += 1
        return kfile
    else:

        lg.debug("file exists, but is it still the same file?")
        file_may_have_changed = False

        # see if the file might have changed
        #print(kfile.mtime)
        #print(get_mtime(filename))
        timediff = abs(kfile.mtime - get_mtime(filename))
        maxtimediff = float(app.conf.get('max_timediff', 0.5))

        if timediff > maxtimediff:
            lg.debug("time stamp has changed (with %.2f seconds)", timediff)
            file_may_have_changed = True
            # even if the checksum turns out ok later, ensure the
            # mtime in the datbase is correct
            kfile.mtime = get_mtime(filename)

        elif filesize != kfile.size:
            lg.debug("file size change %d -> %d", kfile.size, filename.getsize())
            file_may_have_changed = True

        if not file_may_have_changed:
            lg.debug("File is unchanged - leave it as is")
            kfile._state = KFILE_STATE_EXISTS_UNCHANGED
            app.counter['indb'] += 1
            return kfile

        lg.debug("File '%s' still might have changed, check checksum",
                 filename.basename())

        #store old hash object to compare against
        old_khash = kfile.khash

        # # calculate a new khash
        app.counter['hash'] += 1
        app.counter['hashsize'] += filesize
        new_khash = get_khash(app, filename, basename, filesize)

        if new_khash.sha256 == old_khash.sha256:
            lg.debug("Checksums match, no change")
            kfile._state = KFILE_STATE_EXISTS_UNCHANGED
            return kfile


        kfile._state = KFILE_STATE_EXISTS_CHANGED
        app.counter['change'] += 1
        lg.warning("file %s has changed! (%s -> %s)",
                   filename.basename(), old_khash.short, new_khash.short)

        # create a transaction to store the file change
        session  = app.db_session

        tract = get_transaction('<file change>', hostname = kfile.hostname,
                                time_start = kfile.mtime,
                                time_stop = get_mtime(filename),
                                cwd = Path(kfile.filename).dirname())

        session.add(tract)
        session.add(KTransactionIO(iotype = 'input',
                                   ioname = 'input',
                                   ktransaction = tract,
                                   khash = old_khash))
        session.add(KTransactionIO(iotype = 'output',
                                   ioname = 'output',
                                   ktransaction = tract,
                                   khash = new_khash))

        if not old_khash in kfile.khash_history:
            kfile.khash_history.append(old_khash)

        #remember the change for this session
        kfile.old_khash = old_khash
        kfile.khash = new_khash
        kfile.mtime = get_mtime(filename)
        app.db_session.add(new_khash)

        lg.info("Copying over old keyvals to new khash")

        # copy old data to new khash
        for kv in old_khash.keyvals:
            kfile_set(app, kfile, kv.key, kv.val)

        return kfile


def get_token_khash(app, category, uid=None, hooks=True):
    """return a khash for a (non existing) file representing an
    internal object, such as for example a transaction.

    This allows kea to attach key value pairs to objects as well as
    files.

    if uid is None, a random uid is generated
    """
    if uid is None:
        uid = util.get_random_id()

    txt = '{} {}'.format(category, uid).encode('UTF-8')
    handle = io.BytesIO(txt)
    handle.seek(0)

    return get_khash_filehandle(app, handle, hooks,
                                arcdata = dict(
                                    size = len(txt),
                                    mtime = datetime.datetime.now(),
                                    name = 'token:{}:{}'.format(category, uid)))


def get_khash_filehandle(app, filehandle, hooks=True, arcdata=None):
    khash = get_kfile_2(app, filehandle, arcdata=arcdata)
    if hooks:
        app.run_hook('load_khash',
                     khash, reference_path=arcdata['reference_path'])
    return khash


def get_kfile(app, filename, hooks=True):
    """
    filename is either a file on disk or a file-like object (has a read function)
    """
    kfile = get_kfile_2(app, filename)

    kfile._app = app

    #append a setter method
    def setter(self, key, val, *args, **kwargs):
        kfile_set(self._app, self, key, val, *args, **kwargs)

    kfile.set = types.MethodType(setter, kfile)

    if not kfile['basename']:
        kfile.set('basename', Path(filename).basename())

    if hooks:
        app.run_hook('load_kfile', kfile)

    return kfile


def get_khash(app, filename, basename, filesize, is_handle=False):
    """
    Calculate a new checksum & add create or retrieve a new khash object

    Note - this object does not add a hash to the session - that's up to
    calling routines - sometimes it is not required.

    filename is either a Path or file like object
    """

    session = app.db_session

    if is_handle:
        lg.debug(f"find hash for filehandle {basename}")
    else:
        lg.debug(f"find hash for file {filename}")
        assert isinstance(filename, Path)

    hashes = dict(
        sha256=hashlib.sha256(),
        md5=hashlib.md5(),
        sha1=hashlib.sha1())

    block_size = 2 ** 20
    if is_handle:
        while True:
            block = filename.read(block_size)
            if not block:
                break
            [v.update(block) for v in hashes.values()]
    else:
        with open(filename, "rb") as F:
            while True:
                block = F.read(block_size)
                if not block:
                    break
                [v.update(block) for v in hashes.values()]


    return_hashes = {}
    return_hashes['short'] = short = util.file_checksum_to_short_id(hashes['sha256'])
    for k, v in hashes.items():
        hd = v.hexdigest()
        return_hashes[k] = hd

        if is_handle:
            lg.debug(f"{k} of handle {basename} is: {hd[:5]}..{hd[-5:]}")
        else:
            lg.debug(f"{k} of {filename.basename()} is: {hd[:5]}..{hd[-5:]}")

    # first check if the hash exists:
    try:
        khash = session.query(KHash).filter_by(sha256 = return_hashes['sha256']).one()
    except NoResultFound:
        # create a new record
        khash = KHash(sha256 = return_hashes['sha256'],
                      sha1 = return_hashes['sha1'],
                      md5 = return_hashes['md5'],
                      short = return_hashes['short'],
                      size = filesize
        )

    return khash


class NoTransactionFound(Exception):
    """ No Transaction found in this job"""
    pass


def find_khash(app: fantail.app,
               short: str = None,
               sha256: str = None):

    session = app.db_session
    qargs = {}
    if not short is None:
        qargs['short'] = short
    elif sha256 is not None:
        qargs['sha256'] = sha256
    else:
        raise Exception("No hash requested")

    hashes = session.query(KHash).filter_by(
        **qargs).all()

    assert len(hashes) < 2
    if len(hashes) == 0: return
    return hashes[0]



def find_transaction(app, transaction_id):
    """Find a transaction in the database"""
    session = app.db_session
    tracts = session.query(KTransaction).filter_by(
        uid = transaction_id).all()
    assert len(tracts) < 2

    if len(tracts) == 0:
        return
    return tracts[0]
