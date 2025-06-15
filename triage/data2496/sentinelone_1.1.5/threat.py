class Threat:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.whiteningOptions = kwargs.get('whiteningOptions', None)
        self.mitigationStatus = [ThreatMitigationStatus(**status) for status in kwargs.get('mitigationStatus', [])]
        self.indicators = [ThreatIndicator(**indicator) for indicator in kwargs.get('indicators', [])]
        self.containerInfo = ThreatContainerInfo(**kwargs.get('containerInfo', {}))
        self.kubernetesInfo = ThreatKubernetesInfo(**kwargs.get('kubernetesInfo', {}))
        self.threatInfo = ThreatInfo(**kwargs.get('threatInfo', {}))
        self.agentRealtimeInfo = ThreatAgentRealtimeInfo(**kwargs.get('agentRealtimeInfo', {}))
        self.agentDetectionInfo = ThreatAgentDetectionInfo(**kwargs.get('agentDetectionInfo', {}))


class ThreatMitigationStatus:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', None)
        self.action = kwargs.get('action', None)
        self.lastUpdate = kwargs.get('lastUpdate', None)


class ThreatIndicator:
    def __init__(self, **kwargs):
        self.ids = kwargs.get('ids', None)
        self.category = kwargs.get('category', None)
        self.description = kwargs.get('description', None)
        self.tactics = kwargs.get('tactics', None)


class ThreatContainerInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.image = kwargs.get('image', None)
        self.labels = kwargs.get('labels', None)


class ThreatKubernetesInfo:
    def __init__(self, **kwargs):
        self.cluster = kwargs.get('cluster', None)
        self.namespace = kwargs.get('namespace', None)
        self.pod = kwargs.get('pod', None)
        self.node = kwargs.get('node', None)
        self.namespaceLabels = kwargs.get('namespaceLabels', None)
        self.podLabels = kwargs.get('podLabels', None)
        self.controllerKind = kwargs.get('controllerKind', None)
        self.controllerName = kwargs.get('controllerName', None)
        self.controllerLabels = kwargs.get('controllerLabels', None)


class ThreatInfo:
    def __init__(self, **kwargs):
        self.threatId = kwargs.get('threatId', None)
        self.analystVerdict = kwargs.get('analystVerdict', None)
        self.analystVerdictDescription = kwargs.get('analystVerdictDescription', None)
        self.browserType = kwargs.get('browserType', None)
        self.collectionId = kwargs.get('collectionId', None)
        self.certificateId = kwargs.get('certificateId', None)
        self.classification = kwargs.get('classification', None)
        self.classificationSource = kwargs.get('classificationSource', None)
        self.confidenceLevel = kwargs.get('confidenceLevel', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.mitigatedPreemptively = kwargs.get('mitigatedPreemptively', None)
        self.detectionType = kwargs.get('detectionType', None)
        self.engines = kwargs.get('engines', None)
        self.fileExtensionType = kwargs.get('fileExtensionType', None)
        self.filePath = kwargs.get('filePath', None)
        self.fileSize = kwargs.get('fileSize', None)
        self.fileVerificationType = kwargs.get('fileVerificationType', None)
        self.identifiedAt = kwargs.get('identifiedAt', None)
        self.initiatedBy = kwargs.get('initiatedBy', None)
        self.initiatedByDescription = kwargs.get('initiatedByDescription', None)
        self.initiatingUserId = kwargs.get('initiatingUserId', None)
        self.initiatingUsername = kwargs.get('initiatingUsername', None)
        self.isValidCertificate = kwargs.get('isValidCertificate', None)
        self.isFileless = kwargs.get('isFileless', None)
        self.reachedEventsLimit = kwargs.get('reachedEventsLimit', None)
        self.maliciousProcessArguments = kwargs.get('maliciousProcessArguments', None)
        self.md5 = kwargs.get('md5', None)
        self.originatorProcess = kwargs.get('originatorProcess', None)
        self.publisherName = kwargs.get('publisherName', None)
        self.sha1 = kwargs.get('sha1', None)
        self.sha256 = kwargs.get('sha256', None)
        self.mitigationStatus = kwargs.get('mitigationStatus', None)
        self.mitigationStatusDescription = kwargs.get('mitigationStatusDescription', None)
        self.threatName = kwargs.get('threatName', None)
        self.incidentStatus = kwargs.get('incidentStatus', None)
        self.incidentStatusDescription = kwargs.get('incidentStatusDescription', None)
        self.storyline = kwargs.get('storyline', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.externalTicketId = kwargs.get('externalTicketId', None)
        self.externalTicketExists = kwargs.get('externalTicketExists', None)
        self.automaticallyResolved = kwargs.get('automaticallyResolved', None)
        self.cloudFilesHashVerdict = kwargs.get('cloudFilesHashVerdict', None)
        self.highestMitigationReport = kwargs.get('highestMitigationReport', None)
        self.pendingActions = kwargs.get('pendingActions', None)
        self.rebootRequired = kwargs.get('rebootRequired', None)
        self.failedActions = kwargs.get('failedActions', None)
        self.processUser = kwargs.get('processUser', None)


class ThreatAgentRealtimeInfo:
    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId', None)
        self.accountName = kwargs.get('accountName', None)
        self.siteId = kwargs.get('siteId', None)
        self.siteName = kwargs.get('siteName', None)
        self.groupId = kwargs.get('groupId', None)
        self.groupName = kwargs.get('groupName', None)
        self.activeThreats = kwargs.get('activeThreats', None)
        self.agentDomain = kwargs.get('agentDomain', None)
        self.agentId = kwargs.get('agentId', None)
        self.agentIsActive = kwargs.get('agentIsActive', None)
        self.agentIsDecommissioned = kwargs.get('agentIsDecommissioned', None)
        self.agentDecommissionedAt = kwargs.get('agentDecommissionedAt', None)
        self.agentMachineType = kwargs.get('agentMachineType', None)
        self.agentNetworkStatus = kwargs.get('agentNetworkStatus', None)
        self.agentOsName = kwargs.get('agentOsName', None)
        self.agentOsType = kwargs.get('agentOsType', None)
        self.agentOsRevision = kwargs.get('agentOsRevision', None)
        self.agentUuid = kwargs.get('agentUuid', None)
        self.agentComputerName = kwargs.get('agentComputerName', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.userActionsNeeded = kwargs.get('userActionsNeeded', None)
        self.scanStatus = kwargs.get('scanStatus', None)
        self.scanStartedAt = kwargs.get('scanStartedAt', None)
        self.scanFinishedAt = kwargs.get('scanFinishedAt', None)
        self.scanAbortedAt = kwargs.get('scanAbortedAt', None)
        self.mitigationMode = kwargs.get('mitigationMode', None)
        self.networkInterfaces = kwargs.get('networkInterfaces', None)
        self.agentInfected = kwargs.get('agentInfected', None)


class ThreatAgentDetectionInfo:
    def __init__(self, **kwargs):
        self.groupId = kwargs.get('groupId', None)
        self.groupName = kwargs.get('groupName', None)
        self.siteId = kwargs.get('siteId', None)
        self.siteName = kwargs.get('siteName', None)
        self.accountId = kwargs.get('accountId', None)
        self.accountName = kwargs.get('accountName', None)
        self.agentIpV4 = kwargs.get('agentIpV4', None)
        self.agentIpV6 = kwargs.get('agentIpV6', None)
        self.agentDomain = kwargs.get('agentDomain', None)
        self.externalIp = kwargs.get('externalIp', None)
        self.agentUuid = kwargs.get('agentUuid', None)
        self.agentLastLoggedInUserName = kwargs.get('agentLastLoggedInUserName', None)
        self.agentOsRevision = kwargs.get('agentOsRevision', None)
        self.agentOsName = kwargs.get('agentOsName', None)
        self.agentRegisteredAt = kwargs.get('agentRegisteredAt', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.agentMitigationMode = kwargs.get('agentMitigationMode', None)
        self.agentDetectionState = kwargs.get('agentDetectionState', None)
        self.cloudProviders = kwargs.get('cloudProviders', None)


class ThreatGroup:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.whiteningOptions = kwargs.get('whiteningOptions', None)
        self.mitigationStatus = [ThreatMitigationStatus(**status) for status in kwargs.get('mitigationStatus', [])]
        self.containerInfo = ThreatContainerInfo(**kwargs.get('containerInfo', {}))
        self.kubernetesInfo = ThreatKubernetesInfo(**kwargs.get('kubernetesInfo', {}))
        self.threatInfo = ThreatInfo(**kwargs.get('threatInfo', {}))
        self.agentRealtimeInfo = ThreatAgentRealtimeInfo(**kwargs.get('agentRealtimeInfo', {}))
        self.agentDetectionInfo = ThreatAgentDetectionInfo(**kwargs.get('agentDetectionInfo', {}))
        self.notMitigated = kwargs.get('notMitigated', None)
        self.mitigated = kwargs.get('mitigated', None)
        self.markedAsBenign = kwargs.get('markedAsBenign', None)
        self.fromSameAgent = kwargs.get('fromSameAgent', None)
        self.collectionId = kwargs.get('collectionId', None)
        self.totalAgents = kwargs.get('totalAgents', None)
        self.groups = kwargs.get('groups', None)
        self.sites = kwargs.get('sites', None)
        self.accounts = kwargs.get('accounts', None)
