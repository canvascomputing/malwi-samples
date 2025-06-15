
import argparse
import base64
from collections import defaultdict
import collections
import copy
from functools import lru_cache
import base58
import glob
import logging
from pprint import pprint
import os
import re
import socket
import sys
import subprocess as sp
import uuid
import re

lg = logging.getLogger(__name__)

from path import Path
import yaml

def get_hostname(app):
    if app.conf.get('hostname'):
        return app.conf['hostname']
    else:
        return socket.gethostname()


dtype_setters = {}

dtype_getters = {
    'int': int,
    'float': float,
}

dtype_formatters = {
    'set': lambda val: "|".join(sorted(list(val))),
    'float': lambda val: "{.2f}".format(val),
    }


def get_record_file(rtype, rvalue):

    assert re.match(r'[a-zA-Z0-9_]+', rtype)
    assert re.match(r'[a-zA-Z0-9_]+', rvalue)

    recpath = Path('~/.cache/kea3/records').expanduser()
    recpath /= rtype
    recpath.makedirs_p()
    recfile = recpath / f'record.{rvalue}'

    # always create - small operation & too risky to have go wrong
    with open(recfile, 'w') as F:
        F.write(f'record {rtype} {rvalue}')
    return recfile


def dtype_info(app, key, record_type = None):
    if record_type is None:
        conf = app.conf
    else:
        conf = app.conf['keywords'].get(record_type)

    if not key in conf['keywords']:
        raise Exception(f"unknown key: {key}")

    kinfo = conf['keywords'][key]

    if 'alias' in kinfo:
        return dtype_info(app, kinfo['alias'], record_type=record_type)

    kinfo['dtype'] = kinfo.get('dtype', 'str')
    kinfo['cardinality'] = kinfo.get('cardinality', '1')
    kinfo['setter'] = dtype_setters.get(kinfo['dtype'], str)
    kinfo['getters'] = dtype_getters.get(kinfo['dtype'], str)
    kinfo['formatter'] = dtype_formatters.get(kinfo['dtype'], str)
    return key, kinfo



def get_io_info(job, ret_atype=None):
    for dname, dinfo in job['_params'].items():
        atype = dinfo['atype']
        #print(atype)
        if atype not in ['input', 'output']:
            continue

        if ret_atype is not None and ret_atype != atype:
            continue

        value = job[dname]
        if isinstance(value, list):
            for v in value:
                yield atype, dname, v
        else:
            yield atype, dname, value


def file_checksum_to_short_id(c):
#    rv = 'f' + base58.b58encode(c.digest()).decode('UTF-8')[:11]
    rv = 'f' + c.hexdigest()[:11]
    return rv


def get_random_id():
    rv = base58.b58encode(uuid.uuid4().bytes).decode('UTF-8')[:11]
    return rv


def get_randon_transaction_id():
    return 't' + get_random_id()


def get_executor_name(app):
    executor_name = app.conf.get('default_executor', 'simple')

    #anything on the command line??
    if '-x' in sys.argv:
        xloc = sys.argv.index('-x')
        executor_name = sys.argv[xloc+1]

    return executor_name


def recursive_dict_copy(incoming):
    from kea3 import models
    rv = {}
    for k, v in incoming.items():
        if isinstance(v, collections.Mapping):
            rv[k] = recursive_dict_copy(incoming[k])
        elif isinstance(v, models.KFile):
            #don't copy KFiles
            rv[k] = v
        else:
            rv[k] = copy.copy(v)
    return rv


#thanks: https://stackoverflow.com/a/3233356/234172
def recursive_dict_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = recursive_dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


## log files
def get_latest_log(path):
    logdir = Path(path) / '.kea3/log'
    if not logdir.exists():
        lg.warning("No logs found")
        return {}

    rv = sp.check_output('ls -t {} | head -1'.format(logdir), shell=True)
    rv = rv.strip().decode()
    with open(logdir / rv) as F:
        return yaml.load(F)
