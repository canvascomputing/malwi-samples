import string
import time
import uuid

import six

from management.mgmtsdk_v2.entities.deep_visibility_v2 import get_random_string


class Ioc(object):
    def __init__(self, randomize_empty=True, **kwargs):
        self.externalId = kwargs.get('externalId', str(uuid.uuid4()) if randomize_empty else None)
        self.source = kwargs.get('source', get_random_string() if randomize_empty else None)
        self.type = kwargs.get('type', IocType.DNS if randomize_empty else None)
        self.value = kwargs.get('value', get_random_string() if randomize_empty else None)
        self.method = kwargs.get('method', IocMethod.EQUALS if randomize_empty else None)
        self.name = kwargs.get('name', get_random_string() if randomize_empty else None)
        self.description = kwargs.get('description', get_random_string() if randomize_empty else None)
        self.category = kwargs.get('category', [IocCategory.THREATS] if randomize_empty else [])
        self.patternType = kwargs.get('patternType', get_random_string() if randomize_empty else None)
        self.pattern = kwargs.get('pattern', get_random_string() if randomize_empty else None)
        self.validUntil = kwargs.get('validUntil', int((time.time() + 60 * 60 * 48) * 1000) if randomize_empty else None)  # Now + 48 Hours
        self.creationTime = kwargs.get('creationTime', int(time.time() * 1000) if randomize_empty else None)
        self.metadata = kwargs.get('metadata', get_random_string() if randomize_empty else None)
        self.mitreTactic = kwargs.get('mitreTactic', [get_random_string(10, chars=string.ascii_letters),
                                                      get_random_string(10)] if randomize_empty else [])
        self.intrusionSets = kwargs.get('intrusionSets', [get_random_string(10, chars=string.ascii_letters),
                                                          get_random_string(10)] if randomize_empty else [])
        self.reference = kwargs.get('reference', [get_random_string(10, chars=string.ascii_letters),
                                                  get_random_string(10)] if randomize_empty else [])
        self.threatActors = kwargs.get('threatActors',[get_random_string(10, chars=string.ascii_letters),
                                                       get_random_string(10)] if randomize_empty else [])
        self.creator = kwargs.get('creator')
        self.createdAt = kwargs.get('createdAt')
        self.batchId = kwargs.get('batchId')
        self.uuid = kwargs.get('uuid')
        self.scope = kwargs.get('scope')
        self.scopeId = kwargs.get('scopeId')
        self.updatedAt = kwargs.get('updatedAt')

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class IocMethod(object):
    EQUALS = 'EQUALS'


class IocType(object):
    IPV4 = 'IPV4'
    IPV6 = 'IPV6'
    DNS = 'DNS'
    URL = 'URL'
    SHA1 = 'SHA1'
    SHA256 = 'SHA256'
    MD5 = 'MD5'


class IocCategory(object):
    THREATS = 'threats'
