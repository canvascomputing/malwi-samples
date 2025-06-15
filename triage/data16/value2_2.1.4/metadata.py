
from datetime import datetime
import logging
import os
from pprint import pprint
import sys
import time

import fantail
import humanfriendly
from path import Path

from kea3 import kmeta, util
import kea3.models as km

lg = logging.getLogger(__name__)


@fantail.arg("filename", nargs="+")
@fantail.arg("val")
@fantail.arg("key")
@fantail.commandName("set")
def keaset(app, args):
    """Set a key/value pair on a file"""
    key, val = args.key, args.val

    for filename in args.filename:
        filename = Path(filename)
        if filename.isdir():
            # save to k3.config file
            lg.debug(f"Setting '{key}'='{val}' to folder: '{filename}/k3.meta'")
            kmeta.k3meta_set(app, filename, key, val)
        else:
            lg.debug(f"Setting '{key}'='{val}' to file: '{filename}'")
            kfile = kmeta.get_kfile(app, filename)
            kfile.set(key, val)

@fantail.arg("filename", nargs="+")
@fantail.commandName("save")
def keasave(app, args):
    """Ensure metadata is saved for this file"""
    for filename in args.filename:
        kfile = kmeta.get_kfile(app, filename)


@fantail.arg("val")
@fantail.arg("key")
@fantail.arg("record_name")
@fantail.arg("record_type")
@fantail.commandName("rset")
def kearecordset(app, args):
    """Set a key/value pair on a record"""

    #create or find a temp file
    key, val = args.key, args.val
    rtype, rname = args.record_type, args.record_name
    rfile = util.get_record_file(rtype, rname)
    kfile = kmeta.get_kfile(app, rfile)
    kfile.set(key, val, record_type = rtype)


@fantail.arg("record_name")
@fantail.arg("record_type")
@fantail.commandName("rshow")
def kearecordshow(app, args):
    """Show data for a record"""
    rtype, rname = args.record_type, args.record_name
    rfile = util.get_record_file(rtype, rname)
    kfile = kmeta.get_kfile(app, rfile)
    for kv in kfile.khash.keyvals:
        if kv.key in ['size', 'basename']: continue
        print(f"{kv.key}\t{kv.val}")


@fantail.arg("filename")
@fantail.arg("key")
@fantail.commandName("get")
def keaget(app, args):
    """Return the value of a key associated with a file"""
    key = args.key
    kname, kinfo = util.dtype_info(app, key)
    filename = args.filename
    kfile = kmeta.get_kfile(app, filename)
    vals = kfile.get(key)
    if len(vals) == 0:
        print('<undefined>')
    else:
        print(", ".join(sorted(vals)))


@fantail.arg("filename", nargs='+')
@fantail.command
def forget(app, args):
    """Forget about this file (not the hash)"""
    session = app.db_session
    for filename in args.filename:
        kfile = kmeta.get_kfile(app, filename)
        session.delete(kfile)


@fantail.arg("filename", nargs="+")
@fantail.arg("key")
@fantail.command
def unset(app, args):
    """Remove a key/value pair from this file (and all files with the same checksum)"""

    key = args.key
    if '=' in key:
        key, val = key.split('=')
    else:
        val = None

    kname, kinfo = util.dtype_info(app, key)
    for filename in args.filename:
        kfile = kmeta.get_kfile(app, filename)
        kmeta.kfile_unset(app, kfile, kname, val=val)


@fantail.arg("filename")
@fantail.command
def sha1(app, args):
    """Show the sha1 of a file"""
    filename = args.filename
    kfile = kmeta.get_kfile(app, filename)
    print(kfile.khash.sha1)


@fantail.command
def scan(app, args):

    import fnmatch

    t = time.time()
    toprint = ""

    #find ignore files
    curpath = Path('.').abspath()
    app.api.remove_deleted_kfiles_from_path(app, curpath)

    toignore = set(['.git', '*.pyc'])
    while True:
        ignorefile = curpath / '.k3ignore'
        if ignorefile.exists():
            lg.debug("loading ignore file %s", ignorefile)
            with open(ignorefile) as F:
                for line in F:
                    line = line.strip()
                    if not line:
                        continue
                    toignore.add(line)
        curpath = curpath.dirname()
        if curpath == '/': break

    for root, dirs, files in os.walk("."):

        dir2remove = set()
        for ignore in toignore:
            files = [x for x in files if not fnmatch.fnmatch(x, ignore)]

            # more cumbersome as dirs needs to be edited in place
            dir2remove |= set([x for x in dirs if fnmatch.fnmatch(x, ignore)])


        for d in list(dir2remove):
            print(d)
            while d in dirs:
                dirs.remove(d)


        for name in files:
            if name.startswith('.'): continue
            if name.endswith('~'): continue
            try:
                kmeta.get_kfile(app, os.path.join(root, name))
            except FileNotFoundError:
                app.counter['notfound'] += 1
            if time.time() - t > 0.1 and not '-q' in sys.argv:
                f = lambda a,b:  humanfriendly.format_size(b) if 'size' in a else b
                toprint = " ".join([f"{a}:{f(a,b)}" for (a,b) in sorted(app.counter.items())])
                sys.stdout.write(toprint + " " * 10 + "\r")
                t = time.time()
    if not '-q' in sys.argv and toprint:
        print()
    for k, v in sorted(app.counter.items()):
        if 'size' in k:
            v = humanfriendly.format_size(v)
        print("{:10s}: {}".format(k, v))


@fantail.commandName('keywords')
def keakeywords(app, args):
    kw = app.conf['keywords']
    for k, v in kw.items():
        print(k)
    
@fantail.arg("filename")
@fantail.commandName("sha256")
def keasha256(app, args):
    """Show the sha256 of a file"""
    filename = args.filename
    kfile = kmeta.get_kfile(app, filename)
    print(kfile.khash.sha256)


@fantail.api
def kea_print_dir(app, dirname):
    for kfile in app.api.get_kfiles_path(app, dirname):
        print(kfile)

@fantail.arg("filename")
@fantail.commandName("show")
def keashow(app, args):
    """Show all data on a give file"""

    filename = Path(args.filename)
    inkfile = None

    if filename.exists() and filename.isfile():
        inkfile = kfile = kmeta.get_kfile(app, filename)
        khash = kfile.khash
    elif filename.exists() and filename.isdir():
        #process directory
        app.api.kea_print_dir(app, filename)
        return
    elif (not filename.exists()) and len(filename) == 12 and filename[0] == 'f':
        #try as a short id
        khash = kmeta.find_khash(app, short=filename)
    elif not filename.exists():
        #file does not exist!
        app.error("Cannot find file", filename)
        return

    print(f"sha256     : {khash.sha256}")
    print(f"sha1       : {khash.sha1}")
    print(f"short      : {khash.short}")
    print(f"md5        : {khash.md5}")

    print("# Files (mtime, hostname, path)")
    if len(khash.files) == 0:
        print(" <no known copies in database>")
    else:
        for kf in khash.files:
            if kf == inkfile:
                times = datetime.fromtimestamp(kf.mtime).isoformat()
                print(f"{times}\t{kf.hostname}\t{kf.filename} **")
            else:
                print(f"{kf.mtime}\t{kf.hostname}\t{kf.filename}")

    if len(khash.keyvals) > 0:
        print("# Metadata:")
        for kv in khash.keyvals:
            kname, kinfo = util.dtype_info(app, kv.key)
            if kinfo['dtype'] == 'record':
                strfmt = kinfo.get('strfmt')
                rfile = util.get_record_file(kv.key, kv.val)
                krfile = kmeta.get_kfile(app, rfile)
                if strfmt is None:
                    vstr = kv.val
                else:
                    # trick - when values are not specified, replace by <key>
                    # better output
                    class Defdict(dict):
                        def __missing__(self, key):
                            return f'<{key}>'
                    vstr = f"{kv.val} | " + strfmt.format_map(Defdict(krfile.as_dict()))

                print(f" - {kv.key:10} : {vstr}")

            else:
                print(f" - {kv.key:10} : {kv.val}")


    if inkfile is not None and len(inkfile.khash_history) > 0:
        print("# File hash history (short, sha256)")
        for hh in inkfile.khash_history:
            print(' -', hh.short, ' ', hh.sha256)

    # see if there are transactions associated with this file
    results = []
    for io in khash.io:
        tract = io.ktransaction
        results.append((tract.time_stop, io, tract))

    if results:
        print("# Transactions")
        for _, io, tract in sorted(results, key=lambda x: x[0]):

            ttime = humanfriendly.format_timespan(time.time() - tract.time_stop,
                                                  max_units=1)
            print(" - " + "\t".join(
                map(str, [tract.uid, ttime + ' ago', tract.name,
                          io.iotype, io.ioname])))
