import abc
import datetime
import logging

import six


LOG = logging.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class AbstractClient(object):

    def __init__(self, event_type, timeout=None, logger=None):
        super(AbstractClient, self).__init__()
        self._validate_event_type(event_type)
        self.event_type = event_type
        self.timeout = timeout
        self.logger = logger or LOG

    @staticmethod
    def _validate_event_type(event_type):
        if (not event_type) or (not isinstance(event_type, six.string_types)):
            raise ValueError("'event_type' must be non-empty string")

    @staticmethod
    def _validate_timestamp(timestamp):
        if timestamp.tzinfo is not None:
            raise ValueError("'timestamp' must be UTC and naive")

    def send_event(self, event_data, event_type=None, timestamp=None,
                   timeout=None, logger=None):
        timestamp = timestamp or datetime.datetime.utcnow()
        self._validate_timestamp(timestamp)
        event_type = event_type or self.event_type
        self._validate_event_type(event_type)
        logger = logger or self.logger
        if timeout is None:
            timeout = self.timeout
        self.logger.debug('Sending event: timestamp=%(timestamp)s,'
                          'event_type=%(event_type)s, event=%(event)s'
                          % {'timestamp': timestamp,
                             'event_type': event_type,
                             'event': event_data})
        self._send_event(event_data=event_data, event_type=event_type,
                         timestamp=timestamp, timeout=timeout, logger=logger)
        self.logger.debug('Event successfully sent')

    @abc.abstractmethod
    def _send_event(self, event_data, event_type, timestamp, timeout, logger):
        raise NotImplementedError()
