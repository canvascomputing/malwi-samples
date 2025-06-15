import logging.config

__all__ = (
    'set_up_logging',
)


def set_up_logging(settings):
    logging.config.dictConfig(settings.logging)
