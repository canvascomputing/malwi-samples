import six


class Exclusion(object):

    def __init__(self, **kwargs):
        self.actions = kwargs.get('actions', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.inject = kwargs.get('inject', None)
        self.mode = kwargs.get('mode', None)
        self.osType = kwargs.get('osType', None)
        self.pathExclusionType = kwargs.get('pathExclusionType', None)
        self.scope = kwargs.get('scope', None)
        self.scopeName = kwargs.get('scopeName', None)
        self.source = kwargs.get('source', None)
        self.type = kwargs.get('type', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.userId = kwargs.get('userId', None)
        self.userName = kwargs.get('userName', None)
        self.value = kwargs.get('value', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['createdAt', 'updatedAt']:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
