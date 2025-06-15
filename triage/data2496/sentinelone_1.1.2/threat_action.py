class Enrichments(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.interfaceType = kwargs.get('interfaceType', None)
        self.interfaceGroupingKey = kwargs.get('interfaceGroupingKey', None)
        self.interfaceGroupingKeyLogoId = kwargs.get('interfaceGroupingKeyLogoId', None)
        self.content = kwargs.get('content', None)


class AvailableActions(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.actionTitle = kwargs.get('actionTitle', None)
        self.actionDescription = kwargs.get('actionDescription', None)
        self.actionWarning = kwargs.get('actionWarning', None)
        self.interfaceType = kwargs.get('interfaceType', None)
        self.interfaceGroupingKey = kwargs.get('interfaceGroupingKey', None)
        self.interfaceGroupingKeyLogoId = kwargs.get('interfaceGroupingKeyLogoId', None)
        self.targetType = kwargs.get('targetType', None)
        self.targetValue = kwargs.get('targetValue', None)
        self.customData = kwargs.get('customData', None)
        self.lastInitiatedBy = kwargs.get('lastInitiatedBy', None)
        self.lastInitiatedByEmail = kwargs.get('lastInitiatedByEmail', None)
        self.lastActionStatus = kwargs.get('lastActionStatus',None)
        self.lastActionStatusMessage = kwargs.get('lastActionStatusMessage', None)
        self.lastStatusUpdatedAt = kwargs.get('lastStatusUpdatedAt', None)


class AvailableActionsCount(object):

    def __init__(self, **kwargs):
        self.interfaceGroupingKey = kwargs.get('interfaceGroupingKey', None)
        self.interfaceGroupingKeyLogoId = kwargs.get('interfaceGroupingKeyLogoId', None)
        self.count = kwargs.get('count', None)


class ExecutedActions(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.actionId = kwargs.get('actionId', None)
        self.interfaceGroupingKey = kwargs.get('interfaceGroupingKey', None)
        self.interfaceGroupingKeyLogoId = kwargs.get('interfaceGroupingKeyLogoId', None)
        self.initiatedBy = kwargs.get('initiatedBy', None)
        self.initiatedByEmail = kwargs.get('initiatedByEmail', None)
        self.actionStatus = kwargs.get('actionStatus', None)
        self.actionStatusMessage = kwargs.get('actionStatusMessage', None)
        self.actionTitle = kwargs.get('actionTitle', None)
        self.actionTargetName = kwargs.get('actionTargetName', None)
