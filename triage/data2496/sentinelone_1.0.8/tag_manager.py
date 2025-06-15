import six


class TagManager(object):
    def __init__(self, **kwargs):
        self.affectedScopes = kwargs.get('affectedScopes', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.createdBy = kwargs.get('createdBy', None)
        self.createdById = kwargs.get('createdById', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.key = kwargs.get('key', None)
        self.value = kwargs.get('value', None)
        self.scopeLevel = kwargs.get('scopeLevel', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.type = kwargs.get('type', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.updatedBy = kwargs.get('updatedBy', None)
        self.operation = kwargs.get('operation', None)
        self.tagId = kwargs.get('tagId', None)
        self.endpointsInCurrentScope = kwargs.get('endpointsInCurrentScope', None)
        self.totalEndpoints = kwargs.get('totalEndpoints', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['affectedScopes', 'createdAt', 'createdBy', 'createdById', 'id', 'key', 'value', 'description'
                       'scopeId', 'scopeLevel', 'updatedAt', 'updatedBy', 'updatedById']:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
