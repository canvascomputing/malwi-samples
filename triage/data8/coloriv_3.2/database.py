"""Database based on sqlite3."""

import pickle
import sqlite3
import time

from eic_utils import base
from eic_utils.base import colorful_str
from eic_utils.base import procedure

one_million_years = 1e6 * 365.2422 * 86400


class Database(object):
    def __init__(self, path,
                 log_file=None, limitation=200):
        """Initializes database.
        Args:
            path: Path to store database.
            tables: Tables of database.
            log_file: Path to store log, default None. If None, print in cmd.
            limitation: Max length of log in cmd.
        """
        self.path = path
        self.log_f = open(log_file, 'a') if log_file else None
        self.limitation = limitation

        self.add_log('init database at {}'.format(base.get_cur_time()))

        with procedure('init database (#y){}(#)'.format(self.path)):
            self.conn = sqlite3.connect(self.path, check_same_thread=False)
            self.conn.row_factory = lambda cursor, row: {
                col[0]: row[idx]
                for idx, col in enumerate(cursor.description)}
            self.cursor = self.conn.cursor()

        with procedure('init global table'):
            self.create_table(
                'global', 
                'key TEXT NOT NULL PRIMARY KEY',
                'value BLOB', 'time REAL')

    def __del__(self):
        if self.log_f:
            self.log_f.close()
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def add_log(self, cmd, *args):
        """Prints logs in cmd or writes in log file."""
        if not self.log_f:
            print(colorful_str('(#g)SQL(#): >> (#b){} {}'.format(cmd, args)[:self.limitation]))
        else:
            self.log_f.write('#{} @{}: {} {}'.format(
                self.log_cnt, base.get_cur_time(), cmd, args))

    def sync(self):
        self.conn.commit()

    def execute(self, cmd, args, sync=True):
        """Runs sql command."""

        self.add_log(cmd, args)
        result = self.cursor.execute(cmd, args)
        if sync:
            self.sync()
        return result

    def select(self, name, limitation=None, keys='*', 
                     return_dict=True, extra=None):
        """Runs SELECT sql 'SELECT keys FROM name WHERE limitation'.

        Args:
            name: Table name.
            limitation: A Dict follow this format example: limitation = {
                        'a>': 2, 'b=': 3, 'c<=': 4}, which means 'SELECT keys
                        FROM name WHERE a>2 and b=3 and c<=4'.
            keys: A list of str or just a str, indicating which keys to return.
            return_dict: A boolean, if True each row returns as a dict,
                         otherwise a list.
        """

        if isinstance(keys, str):
            keys = [keys]
        cmd = 'SELECT {} FROM {}'.format(','.join(keys), name)
        values = []
        if limitation is not None:
            where = 'WHERE {}'.format(
                ' and '.join(['{}?'.format(key) for key in limitation.keys()])
            )
            cmd = ' '.join([cmd, where])
            values = list(limitation.values())
        if isinstance(extra, str):
            cmd = ' '.join([cmd, extra])

        result = self.execute(cmd, values).fetchall()
        if not return_dict:
            result = [list(x.values()) for x in result]
        return result
    # }}}

    def insert(self, name, rows, force=False):  # {{{
        """ insert into table
            Args:
                name: table name
                rows: dict or list of dict, keys and values of dict are
                    keys and values in tables
        """
        if isinstance(rows, dict):
            rows = [rows]

        data = rows[0]
        place_holder = ','.join([
            '(' + ','.join(['?'] * len(data.keys())) + ')'] * len(rows))

        cmd = 'INSERT OR {} INTO \'{}\' ({}) VALUES {}'.format(
            'REPLACE' if force else 'IGNORE',
            name, ','.join(data.keys()), place_holder
        )

        values = []
        for data in rows:
            values += data.values()
        return self.execute(cmd, tuple(values), sync=True)
    # }}}

    def update(self, name, data, limitation=None):  # {{{
        """ update table set
            Args:
                name: table name
                rows: dict, keys and values of dict are keys and values in tables
                limitation: dict follow this format example:
                    limitation = {
                        'a>': 2,
                        'b=': 3,
                        'c<=', 4,
                    }
        """
        cmd = 'UPDATE {} SET {}'.format(
            name, ','.join(['{}=?'.format(key) for key in data.keys()])
        )
        values = list(data.values())
        if limitation is not None:
            where = 'WHERE {}'.format(
                ' and '.join(['{}?'.format(key) for key in limitation.keys()])
            )
            cmd = ' '.join([cmd, where])
            values += list(limitation.values())
        return self.execute(cmd, values, sync=True)

    # }}}

    def delete(self, name, limitation=None):  # {{{
        """ delete from table
            Args:
                name: table name
                limitation: dict follow this format example:
                    limitation = {
                        'a>': 2,
                        'b=': 3,
                        'c<=', 4,
                    }
        """
        cmd = 'DELETE FROM {}'.format(name)
        values = []
        if limitation is not None:
            where = 'WHERE {}'.format(
                ' and '.join(['{}?'.format(key) for key in limitation.keys()])
            )
            cmd = ' '.join([cmd, where])
            values += list(limitation.values())
        return self.execute(cmd, values, sync=True)
    # }}}

    def count(self, name, limitation=None):  # {{{
        """ select from table

            Args:
                name: table name
                limitation: dict follow this format example:
                    limitation = {
                        'a>': 2,
                        'b=': 3,
                        'c<=', 4,
                    }
        """
        cmd = 'SELECT COUNT(*) FROM \'{}\''.format(name)
        values = []
        if limitation is not None:
            where = 'WHERE {}'.format(
                ' and '.join(['{}?'.format(key) for key in limitation.keys()])
            )
            cmd = ' '.join([cmd, where])
            values = list(limitation.values())

        return self.execute(cmd, values).fetchall()[0][0]
    # }}}

    def create_table(self, name, *sql):  # {{{
        """Initializes a table named 'name'.

        CREATE TABLE IF NOT EXISTS name (sql).
        """

        cmd = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(name, 
            ', '.join('?' * len(sql)))
        values = list(sql)
        self.execute(cmd, values, sync=True)

    def drop_table(self, name):  # {{{
        """ DROP TABLE """
        cmd = 'DROP TABLE {}'.format(name)
        return self.execute(cmd, sync=True)
    # }}}

    def get_global(self, key, default=None):  # {{{
        """ get value of key in db, if not exists return default """
        data = self.select('global', keys='value', limitation={
            'key=': key, 'time>': time.time()}, return_dict=False)
        if len(data) == 0:
            return default
        return pickle.loads(data[0][0])
    # }}}

    def set_global(self, key, value, expired_time=one_million_years):  # {{{
        """ set value of key in db, expired in expired_time later """
        self.insert('global', {'key': key, 'value': pickle.dumps(value),
                               'time': time.time() + expired_time}, force=True)
    # }}}
