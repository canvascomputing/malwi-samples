# -*- coding: utf-8 -*-

from pywe_base import BaseWechat
from pywe_storage import MemoryStorage


class BaseComponentTicket(BaseWechat):
    def __init__(self, appid=None, secret=None, token=None, encodingaeskey=None, storage=None):
        super(BaseComponentTicket, self).__init__()
        self.appid = appid
        self.secret = secret
        self.token = token
        self.encodingaeskey = encodingaeskey
        self.storage = storage or MemoryStorage()

    @property
    def component_verify_ticket_key(self):
        return '{0}:component:verify:ticket'.format(self.appid)

    def update_params(self, appid=None, secret=None, token=None, encodingaeskey=None, storage=None):
        self.appid = appid or self.appid
        self.secret = secret or self.secret
        self.token = token or self.token
        self.encodingaeskey = encodingaeskey or self.encodingaeskey
        self.storage = storage or self.storage
