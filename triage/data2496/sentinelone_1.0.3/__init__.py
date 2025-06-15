import os
import sys
import logging
import tempfile
from logging import FileHandler, Formatter, StreamHandler

logger = logging.getLogger('MgmtSdk')


def _set_default_log_handlers():
    LOG_LEVELS = {'debug': 10, 'info': 20, 'warning': 30, 'warn': 30, 'error': 40}

    tempdir = "/tmp" if sys.platform == 'darwin' else tempfile.gettempdir()  # gettempdir return dummy dir on macos
    default_log_path = os.path.join(tempdir, 'mgmt_sdk.log')

    log_path = os.environ.get('SDK_LOG_PATH', default_log_path)
    log_level = os.environ.get('SDK_LOG_LEVEL', 'debug').lower()

    if log_level not in LOG_LEVELS:
        log_level = 'debug'

    format_string = '[%(name)s][%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'

    file_handler = FileHandler(filename=log_path)
    file_handler.setFormatter(Formatter(format_string))

    stream_handler = StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(Formatter(format_string))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(LOG_LEVELS[log_level])


if os.environ.get('SDK_LOG_DEFAULT_HANDLERS', 'true').lower() == 'true':
    _set_default_log_handlers()
