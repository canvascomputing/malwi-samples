import six


class Location(object):
    def __init__(self, **kwargs):
        self.activeFirewallRules = kwargs.get('activeFirewallRules', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.createdBy = kwargs.get('createdBy', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.description = kwargs.get('description', None)
        self.dnsLookup = kwargs.get('dnsLookup', None)
        self.dnsServers = kwargs.get('dnsServers', None)
        self.editable = kwargs.get('editable', None)
        self.id = kwargs.get('id', None)
        self.ipAddresses = kwargs.get('ipAddresses', None)
        self.isFallback = kwargs.get('isFallback', None)
        self.name = kwargs.get('name', None)
        self.networkInterfaces = kwargs.get('networkInterfaces', None)
        self.operator = kwargs.get('operator', None)
        self.registryKeys = kwargs.get('registryKeys', None)
        self.reportingAgents = kwargs.get('reportingAgents', None)
        self.scope = kwargs.get('scope', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.serverConnectivity = kwargs.get('serverConnectivity', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.updatedBy = kwargs.get('updatedBy', None)
        self.updater = kwargs.get('updater', None)
        self.updaterId = kwargs.get('updaterId', None)


    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['activeFirewallRules', 'createdAt', 'createdBy', 'creatorId',  'editable', 'id',
                       'reportingAgents', 'scope', 'scopeId', 'updatedAt', 'updater',  'updaterId', 'isFallback', ]:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
