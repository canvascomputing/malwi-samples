import six


class Activity(object):
    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId', None)
        self.activityType = kwargs.get('activityType', None)
        self.agentId = kwargs.get('agentId', None)
        self.agentUpdatedVersion = kwargs.get('agentUpdatedVersion', None)
        self.applications = kwargs.get('applications', None)
        self.comments = kwargs.get('comments', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.data = kwargs.get('data', None)
        self.description = kwargs.get('description', None)
        self.groupId = kwargs.get('groupId', None)
        self.hash = kwargs.get('hash', None)
        self.id = kwargs.get('id', None)
        self.osFamily = kwargs.get('osFamily', None)
        self.primaryDescription = kwargs.get('primaryDescription', None)
        self.secondaryDescription = kwargs.get('secondaryDescription', None)
        self.siteId = kwargs.get('siteId', None)
        self.threatId = kwargs.get('threatId', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.userId = kwargs.get('userId', None)

    def to_json(self):
        orig_json = self.__dict__
        del orig_json['createdAt']
        del orig_json['updatedAt']
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class ActivityType(object):
    def __init__(self, **kwargs):
        self.action = kwargs.get('action', None)
        self.descriptionTemplate = kwargs.get('descriptionTemplate', None)
        self.id = kwargs.get('id', None)
