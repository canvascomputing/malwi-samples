
from copy import copy
from datetime import datetime
from path import Path
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import relationship

from . import util

Base = declarative_base()

khash_association_table = Table('khash_history', Base.metadata,
    Column('kfile_id', Integer, ForeignKey('khash.id')),
    Column('khash_id', Integer, ForeignKey('kfile.id'))
)

class KHash(Base):
    __tablename__ = 'khash'
    id = Column(Integer, primary_key = True)

    #hashes to store
    sha256 = Column(String(64), index=True)
    sha1 = Column(String(40), index=True)
    md5 = Column(String(32), index=True)
    short = Column(String(12), index=True)

    #mostly for statistics
    size = Column(BigInteger)

    #foreign keys
    keyvals = relationship("KkeyVal", back_populates='khash')
    files = relationship("KFile", back_populates='khash')
    io = relationship("KTransactionIO", back_populates='khash')

    def __getitem__(self, key, default=None):
        """ Look in the khash.kyevals """
        if key in 'sha1 sha256 md5 short'.split():
            return getattr(self, key)

        rv = []
        for i, kv in enumerate(self.keyvals):
            if kv.key == key:
                rv.append(kv.val)

        if len(rv) == 0: return default
        elif len(rv) == 1: return rv[0]
        else: return rv


    def __repr__(self):
        return '<khash {}>'.format(self.short)

class AggregateStat(Base):
    __tablename__ = 'aggstat'
    id = Column(Integer, primary_key = True)
    level = Column(String(32))
    timestamp = Column(BigInteger, index=True)
    field = Column(String(64), index=True)
    value = Column(String(64), index=True)
    count = Column(BigInteger)
    sum = Column(BigInteger)

    def __repr__(self):
        return f'<agg {self.timestamp} {self.level} {self.field} {self.value} {self.count} {self.sum}>'


class KkeyVal(Base):
    __tablename__ = 'keyval'
    id = Column(Integer, primary_key = True)
    key = Column(String(32), index=True)
    val = Column(String(4096))

    khash_id = Column(Integer, ForeignKey("khash.id"))
    khash = relationship("KHash", back_populates='keyvals')

    def __repr__(self):
        return "<kkeyval {}: {} = {}>".format(
            self.khash.short, self.key, self.val)


class KFile(Base):
    __tablename__ = 'kfile'
    id = Column(Integer, primary_key = True)
    filename = Column(String(4096, convert_unicode=True))
    hostname = Column(String(512, convert_unicode=True))
    size = Column(BigInteger)
    mtime = Column(Float(precision=53))

    # many to one file -> khash
    # one file points to a unique khash
    khash_id = Column(Integer, ForeignKey("khash.id"))
    khash = relationship("KHash", back_populates='files')

    khash_history = relationship("KHash",
                                secondary=khash_association_table)

    def mtime_fmt(self):
        return datetime.fromtimestamp(int(self.mtime)).isoformat()
    
    def as_dict(self, transient=True):
        rv = {}
        if transient:
            rv['filename'] = self.filename
            rv['hostname'] = self.hostname
            rv['size'] = self.size
            rv['mtime'] = self.mtime
            rv['sha256'] = self.khash.sha256
            rv['sha1'] = self.khash.sha1
            rv['md5'] = self.khash.md5
            rv['short'] = self.khash.short
        for kv in self.khash.keyvals:
            if kv.key == 'size' and not transient:
                continue
            rv[kv.key] = kv.val
        return rv

    def as_items(self, transient=True):
        rv = []
        if transient:
            rv.append(('filename', self.filename))
            rv.append(('hostname', self.hostname))
            rv.append(('size', self.size))
            rv.append(('mtime', self.mtime))
            rv.append(('sha256', self.khash.sha256))
            rv.append(('sha1', self.khash.sha1))
            rv.append(('md5', self.khash.md5))
            rv.append(('short', self.khash.short))
        for kv in self.khash.keyvals:
            if kv.key == 'size' and not transient:
                continue
            rv.append((kv.key, kv.val))
        return rv


    def __getitem__(self, key, default=None):
        """ Look in the khash.kyevals """
        if key in 'sha1 sha256 md5 short'.split():
            return getattr(self.khash, key)

        rv = []
        for kv in self.khash.keyvals:
            if kv.key == key:
                rv.append(kv.val)

        if len(rv) == 0: return default
        elif len(rv) == 1: return rv[0]
        else: return rv


    def get(self, key):
        # return a list with the values of that key
        rv = []
        for kv in self.khash.keyvals:
            if kv.key == key:
                rv.append(kv.val)
        return rv


    def __repr__(self):
        return str(Path(self.filename).abspath())

    __str__ = __repr__


Index('kfile_file_index', KFile.filename)
Index('kfile_host_index', KFile.hostname)
Index('kfile_size_index', KFile.size)


class KTransaction(Base):
    __tablename__ = 'ktransaction'
    id = Column(Integer, primary_key = True)
    uid = Column(String(12), index=True, unique=True)
    hostname = Column(String(512), index=True)
    name = Column(String(256), index=True, default="")
    jobname = Column(String(256), index=True, default="")
    step = Column(String(256), index=True, default="")
    job_name = Column(String(256), default="")
    cwd = Column(String(4096))
    time_start = Column(Float) # DateTime(timezone=True), default=datetime.utcnow)
    time_stop = Column(Float) # DateTime(timezone=True), default=datetime.utcnow)
    jobdata = Column(PickleType, default={})
    io = relationship("KTransactionIO", back_populates='ktransaction')


class KTransactionIO(Base):
    __tablename__ = 'ktransaction_io'
    id = Column(Integer, primary_key = True)
    iotype = Column(String(256))
    ioname = Column(String(256))

    ktransaction_id = Column(Integer, ForeignKey("ktransaction.id"))
    ktransaction = relationship("KTransaction", back_populates='io')

    khash_id = Column(Integer, ForeignKey("khash.id"))
    khash = relationship("KHash", back_populates='io')


tables = [
    KHash,
    KkeyVal,
    KFile,
    KTransaction,
    KTransactionIO,
    ]
