import six


class Filter(object):

    def __init__(self, **kwargs):
        self.createdAt = kwargs.get('createdAt', None)
        self.filterFields = kwargs.get('filterFields', None)
        self.frequency = kwargs.get('frequency', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.notifications = kwargs.get('notifications', None)
        self.recipients = kwargs.get('recipients', None)
        self.scopeLevel = kwargs.get('scopeLevel', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.siteId = kwargs.get('siteId', None)
        self.updatedAt = kwargs.get('updatedAt', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['createdAt', 'updatedAt', 'scopeLevel', 'scopeId']:
                del orig_json[key]
        del orig_json['id']
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
