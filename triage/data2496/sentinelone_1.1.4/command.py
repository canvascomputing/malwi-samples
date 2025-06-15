
class Command(object):
    def __init__(self, **kwargs):
        self.acknowledgedAt = kwargs.get('acknowledgedAt', None)
        self.acknowledgement = kwargs.get('acknowledgement', None)
        self.agentId = kwargs.get('agentId', None)
        self.agentUuid = kwargs.get('agentUuid', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.enabled = kwargs.get('enabled', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.notifications = kwargs.get('notifications', None)
        self.parameters = kwargs.get('parameters', None)
        self.sentAt = kwargs.get('sentAt', None)
        self.status = kwargs.get('status', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.userId = kwargs.get('userId', None)
