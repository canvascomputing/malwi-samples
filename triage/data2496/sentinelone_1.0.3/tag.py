import six


class Tag(object):
    def __init__(self, **kwargs):
        self.affectedScopes = kwargs.get('affectedScopes', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.creator = kwargs.get('creator', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.linkedRules = kwargs.get('linkedRules', None)
        self.name = kwargs.get('name', None)
        self.scope = kwargs.get('scope', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.scopeName = kwargs.get('scopeName', None)
        self.selected = kwargs.get('selected', None)
        self.type = kwargs.get('type', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.updater = kwargs.get('updater', None)
        self.updaterId = kwargs.get('updaterId', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['affectedScopes', 'createdAt', 'creator', 'creatorId', 'id', 'linkedRules',
                       'scope', 'scopeName', 'updatedAt', 'updater', 'updaterId']:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
