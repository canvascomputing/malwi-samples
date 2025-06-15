
class Report(object):

    def __init__(self, **kwargs):
        self.attachmentTypes = kwargs.get('attachmentTypes', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.creatorName = kwargs.get('creatorName', None)
        self.frequency = kwargs.get('frequency', None)
        self.fromDate = kwargs.get('fromDate', None)
        self.id = kwargs.get('id', None)
        self.insightTypes = kwargs.get('insightTypes', None)
        self.interval = kwargs.get('interval', None)
        self.name = kwargs.get('name', None)
        self.scope = kwargs.get('scope', None)
        self.sites = kwargs.get('sites', None)
        self.status = kwargs.get('status', None)
        self.toDate = kwargs.get('toDate', None)
