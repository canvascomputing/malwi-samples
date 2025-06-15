import six


class Site(object):

    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId', None)
        self.accountName = kwargs.get('accountName', None)
        self.activeLicenses = kwargs.get('activeLicenses', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.creator = kwargs.get('creator', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.description = kwargs.get('description', None)
        self.expiration = kwargs.get('expiration', None)
        self.externalId = kwargs.get('externalId', None)
        self.healthStatus = kwargs.get('healthStatus', None)
        self.id = kwargs.get('id', None)
        self.inherits = kwargs.get('inherits', None)
        self.isDefault = kwargs.get('isDefault', None)
        self.licenses = kwargs.get('licenses', None)
        self.name = kwargs.get('name', None)
        self.policy = kwargs.get('policy', None)
        self.registrationToken = kwargs.get('registrationToken', None)
        self.siteType = kwargs.get('siteType', None)
        self.state = kwargs.get('state', None)
        self.suite = kwargs.get('suite', None)
        self.totalLicenses = kwargs.get('totalLicenses', None)
        self.unlimitedExpiration = kwargs.get('unlimitedExpiration', None)
        self.unlimitedLicenses = kwargs.get('unlimitedLicenses', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.user = kwargs.get('user', None)

    def __repr__(self):
        return '<management.mgmtsdk_v2.entities.site.Site:: {}>'.format(self.name)

    def to_json(self):
        orig_json = self.__dict__
        del orig_json['creatorId']
        del orig_json['createdAt']
        del orig_json['updatedAt']
        del orig_json['creator']
        del orig_json['state']
        if hasattr(self, 'policy') and self.policy:
            if not isinstance(self.policy, dict):
                self.policy = self.policy.to_json()
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
