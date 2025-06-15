import logging

import requests

from dpp_client.clients import base

LOG = logging.getLogger(__name__)


class DPPClient(base.AbstractClient):

    def __init__(self, endpoint, event_type, timeout=None, logger=None,
                 adapter_kwargs=None):
        super(DPPClient, self).__init__(event_type, timeout, logger or LOG)
        self.endpoint = endpoint
        self.adapter_kwargs = adapter_kwargs or {}
        self.session = self._get_session()

    @staticmethod
    def _format_timestamp(timestamp):
        return timestamp.isoformat('T') + 'Z'

    def _get_session(self):
        session = requests.Session()
        adapter = requests.sessions.HTTPAdapter(**self.adapter_kwargs)
        session.mount(self.endpoint, adapter)
        return session

    def _send_event(self, event_data, event_type, timestamp, timeout, logger):
        data = {
            'timestamp': self._format_timestamp(timestamp),
            'event_type': event_type,
            'event': event_data,
        }
        resp = self.session.post(self.endpoint, json=data, timeout=timeout)
        resp.raise_for_status()
