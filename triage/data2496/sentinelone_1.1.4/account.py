import six


class Account(object):

    def __init__(self, **kwargs):
        self.accountSfId = kwargs.get('accountSfId', None)
        self.accountType = kwargs.get('accountType', None)
        self.activeLicenses = kwargs.get('activeLicenses', None)
        self.agentsInCoreSku = kwargs.get('agentsInCoreSku', None)
        self.agentsInControlSku = kwargs.get('agentsInControlSku', None)
        self.agentsInCompleteSku = kwargs.get('agentsInCompleteSku', None)
        self.completeSites = kwargs.get('completeSites', None)
        self.controlSites = kwargs.get('controlSites', None)
        self.coreSites = kwargs.get('coreSites', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.creator = kwargs.get('creator', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.expiration = kwargs.get('expiration', None)
        self.externalId = kwargs.get('externalId', None)
        self.id = kwargs.get('id', None)
        self.inherits = kwargs.get('inherits', None)
        self.inUseLicensesComplete = kwargs.get('inUseLicensesComplete', None)
        self.inUseLicensesControl = kwargs.get('inUseLicensesControl', None)
        self.inUseLicensesCore = kwargs.get('inUseLicensesCore', None)
        self.isDefault = kwargs.get('isDefault', None)
        self.name = kwargs.get('name', None)
        self.numberOfUsers = kwargs.get('numberOfUsers', None)
        self.policy = kwargs.get('policy', None)
        self.salesforceId = kwargs.get('salesforceId', None)
        self.skus = kwargs.get('skus', None)
        self.state = kwargs.get('state', None)
        self.totalComplete = kwargs.get('totalComplete', None)
        self.totalControl = kwargs.get('totalControl', None)
        self.totalCore = kwargs.get('totalCore', None)
        self.totalLicenses = kwargs.get('totalLicenses', None)
        self.unlimitedComplete = kwargs.get('unlimitedComplete', None)
        self.unlimitedControl = kwargs.get('unlimitedControl', None)
        self.unlimitedCore = kwargs.get('unlimitedCore', None)
        self.unlimitedExpiration = kwargs.get('unlimitedExpiration', None)
        self.unlimitedLicenses = kwargs.get('unlimitedLicenses', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        if kwargs.get('licenses', None):
            self.licenses = kwargs.get('licenses', None)

    def __repr__(self):
        return f'<management.mgmtsdk_v2.entities.account.Account: {self.name}>'

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['createdAt', 'creator', 'creatorId',  'id', 'isDefault', 'updatedAt', ]:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
