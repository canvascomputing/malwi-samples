import errno
import os
import sys
import time
import traceback
import warnings
from contextlib import contextmanager
from logging.handlers import BaseRotatingHandler, TimedRotatingFileHandler
import logging
from  datetime import datetime
import re
from datetime import datetime
import uuid
import threading
import os
from portalocker import LOCK_EX, lock, unlock
from concurrent_log_handler import ConcurrentRotatingFileHandler

class SheinLogWrapper(logging.Formatter):
    def format(self, record):
        record.host = os.getenv('HOSTNAME')
        record.cmdbAppUid = os.getenv('cmdbAppUid')
        record.ip = os.getenv('MY_POD_IP')
        record.paasName = os.getenv('paasName')
        record.cmdbUname = os.getenv('cmdbUname')
        record.cmdbAppName = os.getenv('cmdbAppUname')
        record.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "+0800"
        record.language = 'python'
        record.title = "xxx"
        record.traceID = uuid.uuid4()
        record.current_thread = threading.current_thread().getName()
        return super(SheinLogWrapper, self).format(record)
def log_file_namer(logger_name: str) -> str:
    logger_name,backup_number = logger_name.rsplit(".", maxsplit=1)
    curr_date = date.today().strftime("%Y-%m-%d")  # noqa: DTZ011

    logger_name = logger_name.replace(".log", "")
    return f"{logger_name}.log.{backup_number}"

def getSscCurrentLogFormatter():
    return SheinLogWrapper('{"appName": "%(cmdbAppName)s",'
                    ' "timestamp": "%(timestamp)s",'
                    ' "level": "%(levelname)s",'
                    '"message": "%(message)s",'
                    '"language": "%(language)s",'
                    ' "traceID": "%(traceID)s" ,'
                    ' "type":"EVENT" ,'
                    ' "bizID": "%(traceID)s" ,'
                    ' "host": "%(host)s",'
                    ' "ip":"%(ip)s" ,'
                    ' "cmdbServiceName":"%(cmdbUname)s" ,'
                    ' "cmdbAppName":"%(cmdbAppName)s" ,'
                    ' "logger":"%(cmdbAppName)s" ,'
                    ' "thread":"%(current_thread)s" }'
                    )

has_chown = hasattr(os, "chown")
has_chmod = hasattr(os, "chmod")


class SscConcurrentRotatingFileHandler(ConcurrentRotatingFileHandler):
    """Handler for logging to a set of files, which switches from one file to the
    next when the current file reaches a certain size. Multiple processes can
    write to the log file concurrently, but this may mean that the file will
    exceed the given size.
    """

    def __init__(  # noqa: PLR0913
        self,
        maxBytes=0,
        backupCount=0,
    ):
        curr_date = datetime.now().strftime("%Y-%m-%d")

        cmdbAppUname = os.getenv('cmdbAppUname')
        filename = f"/lingtian/logs/app/INFO.{curr_date}.log"

        if cmdbAppUname is None:
            filename = f"INFO.{curr_date}.log"

        super(SscConcurrentRotatingFileHandler, self).__init__(
           filename=filename,mode="a",maxBytes=maxBytes,backupCount=backupCount
        )
        self.namer = log_file_namer
        self.setFormatter(getSscCurrentLogFormatter())
        self.extMatch = r"^\d{4}-\d{2}-\d{2}.log.\d{1-2}$"
        self.extMatch = re.compile(self.extMatch)

import logging.handlers

logging.handlers.SscConcurrentRotatingFileHandler = SscConcurrentRotatingFileHandler
from concurrent_log_handler.queue import setup_logging_queues

logger = logging.getLogger("ssc_concurrent_logger")
logger.setLevel(logging.DEBUG)  # optional to set this level here
handler = SscConcurrentRotatingFileHandler(maxBytes=1024 * 1024, backupCount=5)
logger.addHandler(handler)
ch = logging.StreamHandler()
logger.addHandler(ch)
setup_logging_queues()

logging.root = logger
def getLogger():
    return  logger




