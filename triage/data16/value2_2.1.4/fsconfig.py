
from functools import lru_cache

import logging

import fantail
from path import Path
from kea3 import kmeta, util, models
import yaml

lg = logging.getLogger(__name__)

#@fantail.hook('init_template')
#def set_config(app, template):
#    data = kmeta.recursive_read_k3meta(app, Path('.').abspath())
#    util.recursive_dict_update(template.config, data)


@fantail.hook('load_kfile')
def kfile_load(app, kfile, reference_path=None):

    if reference_path is None:
        data = kmeta.recursive_read_k3meta(app, Path(kfile.filename).abspath())
    else:
        data = kmeta.recursive_read_k3meta(app, Path(reference_path).abspath())

    for k, v in data.items():
        kname, kinfo = util.dtype_info(app, k)

        if k in app.conf['keywords']:
            lg.debug("Applying from kfile %s=%s", k, v)

        if kinfo.get('cardinality') == '+':
            for vv in v:
                kmeta.kfile_set(app, kfile, k, vv)
        else:
            kmeta.kfile_set(app, kfile, k, v)


@fantail.hook('load_khash')
def khash_load(app, khash, reference_path):
    """ Variant - for when processing a file handle """
    return kfile_load(app, khash, reference_path)
