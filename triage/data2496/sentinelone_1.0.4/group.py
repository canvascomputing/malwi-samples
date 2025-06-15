import six


class Group(object):

    def __init__(self, **kwargs):
        self.createdAt = kwargs.get('createdAt', None)
        self.creator = kwargs.get('creator', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.filterId = kwargs.get('filterId', None)
        self.filterName = kwargs.get('filterName', None)
        self.id = kwargs.get('id', None)
        self.inherits = kwargs.get('inherits', None)
        self.isDefault = kwargs.get('isDefault', None)
        self.name = kwargs.get('name', None)
        self.policy = kwargs.get('policy', None)
        self.rank = kwargs.get('rank', None)
        self.registrationToken = kwargs.get('registrationToken', None)
        self.siteId = kwargs.get('siteId', None)
        self.totalAgents = kwargs.get('totalAgents', None)
        self.type = kwargs.get('type', None)
        self.updatedAt = kwargs.get('updatedAt', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['createdAt', 'updatedAt', 'creator', 'creatorId', 'id', 'isDefault']:
                del orig_json[key]
        if hasattr(self, 'policy') and self.policy:
            if not isinstance(self.policy, dict):
                self.policy = self.policy.to_json()
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class GroupCount(object):
    def __init__(self, **kwargs):
        self.dynamic = kwargs.get('dynamic', None)
        self.static = kwargs.get('static', None)
