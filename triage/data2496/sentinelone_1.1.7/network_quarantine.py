import six


class NQRule(object):

    def __init__(self, **kwargs):
        self.action = kwargs.get('action', None)
        self.application = kwargs.get('application', None)
        self.direction = kwargs.get('direction', None)
        self.editable = kwargs.get('editable', None)
        self.id = kwargs.get('id', None)
        self.localPort = kwargs.get('localPort', None)
        self.localHost = kwargs.get('localHost', None)
        self.location = kwargs.get('location', None)
        self.name = kwargs.get('name', None)
        self.order = kwargs.get('order', None)
        self.osType = kwargs.get('osType', None)
        self.osTypes = kwargs.get('osTypes', None)
        self.profile = kwargs.get('profile', None)
        self.productId = kwargs.get('productId', None)
        self.protocol = kwargs.get('protocol', None)
        self.remoteHost = kwargs.get('remoteHost', None)
        self.remoteHosts = kwargs.get('remoteHosts', None)
        self.remotePort = kwargs.get('remotePort', None)
        self.ruleType = kwargs.get('ruleType', None)
        self.scope = kwargs.get('scope', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.service = kwargs.get('service', None)
        self.status = kwargs.get('status', None)
        self.tag = kwargs.get('tag', None)
        self.tagIds = kwargs.get('tagIds', None)
        self.tagNames = kwargs.get('tagNames', None)
        self.tags = kwargs.get('tags', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['tags', 'tagNames', 'id']:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
