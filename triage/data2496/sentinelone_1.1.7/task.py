

class Task(object):

    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId', None)
        self.accountName = kwargs.get('accountName', None)
        self.agentComputerName = kwargs.get('agentComputerName', None)
        self.agentIsActive = kwargs.get('agentIsActive', None)
        self.agentIsDecommissioned = kwargs.get('agentIsDecommissioned', None)
        self.agentMachineType = kwargs.get('agentMachineType', None)
        self.agentOsType = kwargs.get('agentOsType', None)
        self.agentUuid = kwargs.get('agentUuid', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.detailedStatus = kwargs.get('detailedStatus', None)
        self.errorReason = kwargs.get('errorReason', None)
        self.groupId = kwargs.get('groupId', None)
        self.groupName = kwargs.get('groupName', None)
        self.id = kwargs.get('id', None)
        self.initiatedBy = kwargs.get('initiatedBy', None)
        self.packageFileName = kwargs.get('packageFileName', None)
        self.parentTaskId = kwargs.get('parentTaskId', None)
        self.siteId = kwargs.get('siteId', None)
        self.siteName = kwargs.get('siteName', None)
        self.status = kwargs.get('status', 'created')
        self.type = kwargs.get('type', None)
        self.signature = kwargs.get('scriptResultsSignature', None)
