import six


class RbacRole(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.permissionIds = kwargs.get('permissionIds', None)
        self.description = kwargs.get('description', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['tags', 'tagNames', 'id']:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
