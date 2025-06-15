import json

from management.common.base_entity import BaseEntity


class Package:
    def __init__(self, major, minor, status, file_id):
        self.major = major
        self.minor = minor
        self.status = status
        self.fileId = file_id

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)


class ReOrder:
    def __init__(self, id, order):
        self.id = id
        self.order = order

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)


class UpgradePolicy:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.isActive = kwargs.get('isActive', None)
        self.scopeLevel = kwargs.get('scopeLevel', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.osType = kwargs.get('osType', None)
        self.allEndpoints = kwargs.get('allEndpoints', None)
        self.tags = kwargs.get('tags', None)
        self.package = kwargs.get('package', None)
        self.isScheduled = kwargs.get('isScheduled', None)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
