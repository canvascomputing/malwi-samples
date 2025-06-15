
import logging

import fantail
from datetime import datetime
import networkx as nx
from path import Path
from sqlalchemy.sql.expression import bindparam

import kea3.models as km
from kea3 import kmeta

lg = logging.getLogger(__name__)

#  postgresql+psycopg2://kea:KeaKea42@localhost/keadb


@fantail.command
def show_database_info(app, args): 
    session = app.db_session
    engine = app.db_engine
    for c in km.tables:
        rows = session.query(c).count()
        print(c.__table__, rows)
        head = session.query(c).limit(5).all()
        for r in head:
            print(' - ', r)
            

@fantail.command
def drop_database(app, args):
    """ Drop all tables from the database (!) """
    session = app.db_session
    engine = app.db_engine

    # this to ensure it works for postgresql as well
    from sqlalchemy.schema import DropTable
    from sqlalchemy.ext.compiler import compiles
    
    @compiles(DropTable, "postgresql")
    def _compile_drop_table(element, compiler, **kwargs):
        return compiler.visit_drop_table(element) + " CASCADE"
    
    for c in km.tables:
        try:
            c.__table__.drop(engine)
        except:
            print("fail ", c)


FILE_FORMATS = {
    'graphml': (nx.read_graphml, nx.write_graphml),
    'yaml': (nx.read_yaml, nx.write_yaml),
    'gml': (nx.read_gml, nx.write_gml)
    }


@fantail.arg('outfile', help='Output file to save data to. Extensions: ' +
             " ".join(FILE_FORMATS.keys()))
@fantail.arg("path", help='input file or path', default='')
@fantail.command
def dump(app, args):
    app.api.dump_to_file(app, args.path, args.outfile)


@fantail.api
def dump_to_file(app, inpath, outfile):
    """Export all file & transaction data based on a file or directory"""

    session = app.db_session
    outext = outfile.rsplit('.', 1)[-1]

    if outext not in FILE_FORMATS:
        app.message("forcing format to gml")
        outext = 'gml'
        outfile += '.gml'

    nxwriter = FILE_FORMATS[outext][1]

    G = nx.DiGraph()

    allhash = set()
    alltrans = set()

    inpath = Path(inpath)
    if not inpath.exists():
        app.error(inpath, "does not exist!")
        exit(-1)

    if inpath.isdir():

        # get all kfiles in this path & below
        inpath = inpath.abspath()
        inpath = inpath.rstrip('/') + '/'   # ensure right slash
        kfiles = session.query(km.KFile)\
                        .filter(km.KFile.filename.like(f'{inpath}%'))\
                        .all()
        khashes = set()
        for kfile in kfiles:
            khashes.add(kfile.khash)

    else:

        kfile = kmeta.get_kfile(app, inpath)
        khashes = [kfile.khash]


    def process_khash(khash, depth=0):
        lg.debug('add hash %s', khash.short)
        if khash.short in G:
            return
        if len(khash.files) > 0:
            fname = str(Path(khash.files[0].filename).basename()) \
                    + '\\n' + khash.short
        else:
            fname = khash.short

        files = [f for f in khash.files if Path(f.filename).exists()]
        filesstr = ";".join([Path(f.filename).basename() for f in files])

        #add KV's
        kvs = dict(kmeta.get_keyvals(app, khash, formatted=False))
        G.add_node(khash.short,
                   title=fname,
                   sha256=khash.sha256,
                   sha1=khash.sha1,
                   md5=khash.md5,
                   nofiles=len(files),
                   files=filesstr,
                   depth=depth,
                   type='hash',
                   **kvs)


        allhash.add(khash.short)
        for ioa in khash.io:
            tract = ioa.ktransaction
            if tract.uid in G:
                continue
            lg.debug('add transaction %s',tract.job_name)
            tname = '{}\\n{}'.format(
                tract.name,
                tract.step)
            G.add_node(tract.uid, title=tname,
                       type='transaction',
                       name = tract.name, step=tract.step,
                       hostname = tract.hostname,
                       jobname = tract.job_name,
                       depth = depth + 1,
                       cwd = tract.cwd,
                       timestart = datetime.fromtimestamp(tract.time_start).isoformat(),
                       timestop = datetime.fromtimestamp(tract.time_stop).isoformat())

            for io in tract.io:
                process_khash(io.khash, depth + 2)
                if io.iotype == 'input':
                    G.add_edge(io.khash.short, tract.uid, name=io.ioname,
                               iotype=io.iotype, ioname=io.ioname)
                elif io.iotype == 'output':
                    G.add_edge(tract.uid, io.khash.short, name=io.ioname,
                               iotype=io.iotype, ioname=io.ioname)
                else:
                    ename = io.iotype + "\n" + io.ioname
                    G.add_edge(io.khash.short, tract.uid, name=ename,
                               iotype=io.iotype, ioname=io.ioname)


    for khash in khashes:
        process_khash(khash)


    nxwriter(G, outfile)
