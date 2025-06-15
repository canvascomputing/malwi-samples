import logging
import random
import six
import string

from datetime import datetime, timedelta

logger = logging.getLogger('MgmtSdk')


class QueryStatus(object):
    def __init__(self, **kwargs):
        self.responseLoadingStatus = kwargs.get('responseLoadingStatus', None)
        self.responseState = kwargs.get('responseState', None)


class BasicQuery(object):
    def __init__(self, **kwargs):
        self.createdAt = kwargs.get('createdAt', None)
        self.query = kwargs.get('query', None)
        self.queryId = kwargs.get('queryId', None)


class ProcessTreeQuery(object):
    def __init__(self, **kwargs):
        self.agentUuid = kwargs.get('agentUuid', None)
        self.baseQueryId = kwargs.get('baseQueryId', None)
        self.fromDate = kwargs.get('fromDate', None)
        self.toDate = kwargs.get('toDate', None)
        self.storyline = kwargs.get('storyline', None)
        self.parentUniqueKey = kwargs.get('parentUniqueKey', None)
        self.siteId = kwargs.get('siteId', None)

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class DvQuery(object):
    def __init__(self, **kwargs):
        self.cursor = kwargs.get('cursor', None)
        self.fromDate = kwargs.get('fromDate', None)
        self.groupIds = kwargs.get('groupIds', None)
        self.limit = kwargs.get('limit', None)
        self.query = kwargs.get('query', None)
        self.queryType = kwargs.get('queryType', None)
        self.siteIds = kwargs.get('siteIds', None)
        self.skip = kwargs.get('skip', None)
        self.tenant = kwargs.get('tenant', None)
        self.toDate = kwargs.get('toDate', None)
        self.isVerbose = kwargs.get('isVerbose', None)

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class TimeFrame(object):
    LAST_HOUR = 'Last Hour'
    LAST_24_HOURS = 'Last 24 Hours'
    TODAY = 'Today'
    LAST_48_HOURS = 'Last 48 Hours'
    LAST_7_DAYS = 'Last 7 Days'
    LAST_14_DAYS = 'Last 14 Days'
    LAST_30_DAYS = 'Last 30 Days'
    THIS_MONTH = 'This Month'
    CUSTOM_RANGE = 'Custom Range'

    @staticmethod
    def list_all():
        return [getattr(TimeFrame, attribute) for attribute in dir(TimeFrame) if not attribute.startswith('__')
                and attribute != 'list_all']


EXCLUDED_FIELDS = ['createdAt']  # Fields that should be excluded from Rule.to_json()


class Rule(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.s1ql = kwargs.get('s1ql')
        self.name = kwargs.get('name', get_random_string(10))
        self.description = kwargs.get('description', get_random_string(10))
        self.severity = kwargs.get('severity', RuleSeverity.Low)
        self.queryType = kwargs.get('queryType', RuleQueryType.EVENTS)
        self.expirationMode = kwargs.get('expirationMode', RuleExpirationMode.Temporary)
        self.expiration = kwargs.get('expirationDate') or kwargs.get('expiration', (datetime.now() + timedelta(days=5,
                                                                                                               hours=5))
                                                                     .isoformat() + 'Z') \
            if self.expirationMode == RuleExpirationMode.Temporary else None
        self.status = kwargs.get('status', RuleStatus.Active)
        self.networkQuarantine = kwargs.get('networkQuarantine', False)
        self.treatAsThreat = kwargs.get('treatAsThreat', None)
        self.statusReason = kwargs.get('statusReason')
        self.scope = kwargs.get('scope')
        self.scopeId = kwargs.get('scopeId')
        self.generatedAlerts = kwargs.get('generatedAlerts')
        self.createdAt = kwargs.get('createdAt')

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None and k not in EXCLUDED_FIELDS}
        return non_empty_json


class RuleQueryType(object):
    EVENTS = 'events'
    PROCESS = 'processes'


class RuleSeverity(object):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
    Critical = 'Critical'


class RuleExpirationMode(object):
    Temporary = 'Temporary'
    Permanent = 'Permanent'


class RuleStatus(object):
    Draft = 'Draft'
    Activating = 'Activating'
    Active = 'Active'
    Disabling = 'Disabling'
    Disabled = 'Disabled'
    Deleted = 'Deleted'
    Deleting = 'Deleting'


def get_random_string(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


class Event(object):

    def __init__(self, **kwargs):
        self.activeContentFileId = kwargs.get('activeContentFileId', None)
        self.activeContentHash = kwargs.get('activeContentHash', None)
        self.activeContentPath = kwargs.get('activeContentPath', None)
        self.activeContentSignedStatus = kwargs.get('activeContentSignedStatus', None)
        self.activeContentType = kwargs.get('activeContentType', None)
        self.agentDomain = kwargs.get('agentDomain', None)
        self.agentGroupId = kwargs.get('agentGroupId', None)
        self.agentId = kwargs.get('agentId', None)
        self.agentInfected = kwargs.get('agentInfected', None)
        self.agentIp = kwargs.get('agentIp', None)
        self.agentIsActive = kwargs.get('agentIsActive', None)
        self.agentIsDecommissioned = kwargs.get('agentIsDecommissioned', None)
        self.agentlastonline = kwargs.get('agentlastonline', None)
        self.agentMachineType = kwargs.get('agentMachineType', None)
        self.agentName = kwargs.get('agentName', None)
        self.agentNetworkStatus = kwargs.get('agentNetworkStatus', None)
        self.agentOs = kwargs.get('agentOs', None)
        self.agentTimestamp = kwargs.get('agentTimestamp', None)
        self.agentUuid = kwargs.get('agentUuid', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.attributes = kwargs.get('attributes', None)
        self.childProcCount = kwargs.get('childProcCount', None)
        self.connectionStatus = kwargs.get('connectionStatus', None)
        self.containerId = kwargs.get('containerId', None)
        self.containerImage = kwargs.get('containerImage', None)
        self.containerLabels = kwargs.get('containerLabels', None)
        self.containerName = kwargs.get('containerName', None)
        self.convictedBy = kwargs.get('convictedBy', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.crossProcCount = kwargs.get('crossProcCount', None)
        self.crossProcDupRemoteProcHandleCount = kwargs.get('crossProcDupRemoteProcHandleCount', None)
        self.crossProcDupThreadHandleCount = kwargs.get('crossProcDupThreadHandleCount', None)
        self.crossProcOpenProcCount = kwargs.get('crossProcOpenProcCount', None)
        self.crossProcOutOfStorylineCount = kwargs.get('crossProcOutOfStorylineCount', None)
        self.crossProcThreadCreateCount = kwargs.get('crossProcThreadCreateCount', None)
        self.direction = kwargs.get('direction', None)
        self.dnsCount = kwargs.get('dnsCount', None)
        self.dnsRequest = kwargs.get('dnsRequest', None)
        self.dnsResponse = kwargs.get('dnsResponse', None)
        self.dstIp = kwargs.get('dstIp', None)
        self.dstPort = kwargs.get('dstPort', None)
        self.endpointMachineType = kwargs.get('endpointMachineType', None)
        self.endpointName = kwargs.get('endpointName', None)
        self.endpointOs = kwargs.get('endpointOs', None)
        self.endpointUuid = kwargs.get('endpointUuid', None)
        self.eventSubType = kwargs.get('eventSubType', None)
        self.eventTime = kwargs.get('eventTime', None)
        self.eventType = kwargs.get('eventType', None)
        self.fileCreatedAt = kwargs.get('fileCreatedAt', None)
        self.fileFullName = kwargs.get('fileFullName', None)
        self.fileId = kwargs.get('fileId', None)
        self.fileIsExecutable = kwargs.get('fileIsExecutable', None)
        self.fileLocation = kwargs.get('fileLocation', None)
        self.fileMd5 = kwargs.get('fileMd5', None)
        self.fileModifyAt = kwargs.get('fileModifyAt', None)
        self.fileSha1 = kwargs.get('fileSha1', None)
        self.fileSha256 = kwargs.get('fileSha256', None)
        self.fileSize = kwargs.get('fileSize', None)
        self.fileType = kwargs.get('fileType', None)
        self.id = kwargs.get('id', None)
        self.indicatorCategory = kwargs.get('indicatorCategory', None)
        self.indicatorDescription = kwargs.get('indicatorDescription', None)
        self.indicatorMetadata = kwargs.get('indicatorMetadata', None)
        self.indicatorName = kwargs.get('indicatorName', None)
        self.isSignatureVerified = kwargs.get('isSignatureVerified', None)
        self.isInfected = kwargs.get('isInfected', None)
        self.isStdinRedirected = kwargs.get('isStdinRedirected', None)
        self.lastLoggedInUserName = kwargs.get('lastLoggedInUserName', None)
        self.k8sClusterName = kwargs.get('k8sClusterName', None)
        self.k8sControllerLabels = kwargs.get('k8sControllerLabels', None)
        self.k8sControllerName = kwargs.get('k8sControllerName', None)
        self.k8sControllerType = kwargs.get('k8sControllerType', None)
        self.k8sNamespace = kwargs.get('k8sNamespace', None)
        self.k8sNamespaceLabels = kwargs.get('k8sNamespaceLabels', None)
        self.k8sNode = kwargs.get('k8sNode', None)
        self.k8sPodLabels = kwargs.get('k8sPodLabels', None)
        self.k8sPodName = kwargs.get('k8sPodName', None)
        self.loginsBaseType = kwargs.get('loginsBaseType', None)
        self.loginsUserName = kwargs.get('loginsUserName', None)
        self.md5 = kwargs.get('md5', None)
        self.moduleHash = kwargs.get('moduleHash', None)
        self.moduleMd5 = kwargs.get('moduleMd5', None)
        self.modulePath = kwargs.get('modulePath', None)
        self.moduleSha1 = kwargs.get('moduleSha1', None)
        self.netConnInCount = kwargs.get('netConnInCount', None)
        self.netConnOutCount = kwargs.get('netConnOutCount', None)
        self.netConnStatus = kwargs.get('netConnStatus', None)
        self.netEventDirection = kwargs.get('netEventDirection', None)
        self.networkMethod = kwargs.get('networkMethod', None)
        self.networkSource = kwargs.get('networkSource', None)
        self.networkUrl = kwargs.get('networkUrl', None)
        self.newFileName = kwargs.get('newFileName', None)
        self.objectType = kwargs.get('objectType', None)
        self.oldFileFullName = kwargs.get('oldFileFullName', None)
        self.oldFileMd5 = kwargs.get('oldFileMd5', None)
        self.oldfileMd5 = kwargs.get('oldFileMd5', None)
        self.oldFileName = kwargs.get('oldFileName', None)
        self.oldFileSha1 = kwargs.get('oldFileSha1', None)
        self.oldfileSha1 = kwargs.get('oldFileSha1', None)
        self.oldFileSha256 = kwargs.get('oldFileSha256', None)
        self.oldfileSha256 = kwargs.get('oldFileSha256', None)
        self.parentPid = kwargs.get('parentPid', None)
        self.parentProcessName = kwargs.get('parentProcessName', None)
        self.parentProcessIsMalicious = kwargs.get('parentProcessIsMalicious', None)
        self.parentProcessStartTime = kwargs.get('parentProcessStartTime', None)
        self.parentProcessUniqueKey = kwargs.get('parentProcessUniqueKey', None)
        self.pid = kwargs.get('pid', None)
        self.processCmd = kwargs.get('processCmd', None)
        self.processDisplayName = kwargs.get('processDisplayName', None)
        self.processGroupId = kwargs.get('processGroupId', None)
        self.processImagePath = kwargs.get('processImagePath', None)
        self.processImageSha1Hash = kwargs.get('processImageSha1Hash', None)
        self.processIntegrityLevel = kwargs.get('processIntegrityLevel', None)
        self.processIsMalicious = kwargs.get('processIsMalicious', None)
        self.processIsRedirectedCommandProcessor = kwargs.get('processIsRedirectedCommandProcessor', None)
        self.processIsWow64 = kwargs.get('processIsWow64', None)
        self.processName = kwargs.get('processName', None)
        self.processRoot = kwargs.get('processRoot', None)
        self.processSessionId = kwargs.get('processSessionId', None)
        self.processStartTime = kwargs.get('processStartTime', None)
        self.processSubSystem = kwargs.get('processSubSystem', None)
        self.processUniqueKey = kwargs.get('processUniqueKey', None)
        self.publisher = kwargs.get('publisher', None)
        self.registryChangeCount = kwargs.get('registryChangeCount', None)
        self.registryId = kwargs.get('registryId', None)
        self.registryKeyPath = kwargs.get('registryKeyPath', None)
        self.registryPath = kwargs.get('registryPath', None)
        self.registryUuid = kwargs.get('registryUuid', None)
        self.relatedToThreat = kwargs.get('relatedToThreat', None)
        self.rpid = kwargs.get('rpid', None)
        self.sha256 = kwargs.get('sha256', None)
        self.signatureSignedInvalidReason = kwargs.get('signatureSignedInvalidReason', None)
        self.signedStatus = kwargs.get('signedStatus', None)
        self.signer = kwargs.get('signer', None)
        self.siteId = kwargs.get('siteId', None)
        self.siteName = kwargs.get('siteName', None)
        self.srcIp = kwargs.get('srcIp', None)
        self.srcPort = kwargs.get('srcPort', None)
        self.srcProcActiveContentFileId = kwargs.get('srcProcActiveContentFileId', None)
        self.srcProcActiveContentHash = kwargs.get('srcProcActiveContentHash', None)
        self.srcProcActiveContentPath = kwargs.get('srcProcActiveContentPath', None)
        self.srcProcActiveContentSignedStatus = kwargs.get('srcProcActiveContentSignedStatus', None)
        self.srcProcActiveContentType = kwargs.get('srcProcActiveContentType', None)
        self.srcProcBinaryisExecutable = kwargs.get('srcProcBinaryisExecutable', None)
        self.srcProcCmdLine = kwargs.get('srcProcCmdLine', None)
        self.srcProcCmdScript = kwargs.get('srcProcCmdScript', None)
        self.srcProcCmdScriptIsComplete = kwargs.get('srcProcCmdScriptIsComplete', None)
        self.srcProcCmdScriptOriginalSize = kwargs.get('srcProcCmdScriptOriginalSize', None)
        self.srcProcCmdScriptSha256 = kwargs.get('srcProcCmdScriptSha256', None)
        self.srcProcCmdScriptApplicationName = kwargs.get('srcProcCmdScriptApplicationName', None)
        self.srcProcDisplayName = kwargs.get('srcProcDisplayName', None)
        self.srcProcImageMd5 = kwargs.get('srcProcImageMd5', None)
        self.srcProcImagePath = kwargs.get('srcProcImagePath', None)
        self.srcProcImageSha1 = kwargs.get('srcProcImageSha1', None)
        self.srcProcImageSha256 = kwargs.get('srcProcImageSha256', None)
        self.srcProcIntegrityLevel = kwargs.get('srcProcIntegrityLevel', None)
        self.srcProcIsStorylineRoot = kwargs.get('srcProcIsStorylineRoot', None)
        self.srcProcIsNative64Bit = kwargs.get('srcProcIsNative64Bit', None)
        self.srcProcIsRedirectCmdProcessor = kwargs.get('srcProcIsRedirectCmdProcessor', None)
        self.srcProcName = kwargs.get('srcProcName', None)
        self.srcProcParentImageMd5 = kwargs.get('srcProcParentImageMd5', None)
        self.srcProcParentImagePath = kwargs.get('srcProcParentImagePath', None)
        self.srcProcParentImageSha1 = kwargs.get('srcProcParentImageSha1', None)
        self.srcProcParentImageSha256 = kwargs.get('srcProcParentImageSha256', None)
        self.srcProcParentName = kwargs.get('srcProcParentName', None)
        self.srcProcParentPid = kwargs.get('srcProcParentPid', None)
        self.srcProcParentProcUid = kwargs.get('srcProcParentProcUid', None)
        self.srcProcParentStartTime = kwargs.get('srcProcParentStartTime', None)
        self.srcProcPid = kwargs.get('srcProcPid', None)
        self.srcProcPublisher = kwargs.get('srcProcPublisher', None)
        self.srcProcReasonSignatureInvalid = kwargs.get('srcProcReasonSignatureInvalid', None)
        self.srcProcRelatedToThreat = kwargs.get('srcProcRelatedToThreat', None)
        self.srcProcRpid = kwargs.get('srcProcRpid', None)
        self.srcProcSessionId = kwargs.get('srcProcSessionId', None)
        self.srcProcSignedStatus = kwargs.get('srcProcSignedStatus', None)
        self.srcProcStartTime = kwargs.get('srcProcStartTime', None)
        self.srcProcStorylineId = kwargs.get('srcProcStorylineId', None)
        self.srcProcSubsystem = kwargs.get('srcProcSubsystem', None)
        self.srcProcTid = kwargs.get('srcProcTid', None)
        self.srcProcUser = kwargs.get('srcProcUser', None)
        self.srcProcUid = kwargs.get('srcProcUid', None)
        self.srcProcVerifiedStatus = kwargs.get('srcProcVerifiedStatus', None)
        self.srcProcCmdLine = kwargs.get('srcProcCmdLine', None)
        self.srcProcCmdScript = kwargs.get('srcProcCmdScript', None)
        self.srcProcCmdScriptIsComplete = kwargs.get('srcProcCmdScriptIsComplete', None)
        self.srcProcCmdScriptOriginalSize = kwargs.get('srcProcCmdScriptOriginalSize', None)
        self.srcProcCmdScriptSha256 = kwargs.get('srcProcCmdScriptSha256', None)
        self.srcProcCmdScriptApplicationName = kwargs.get('srcProcCmdScriptApplicationName', None)
        self.srcProcDisplayName = kwargs.get('srcProcDisplayName', None)
        self.srcProcImagePath = kwargs.get('srcProcImagePath', None)
        self.storyline = kwargs.get('storyline', None)
        self.taskName = kwargs.get('taskName', None)
        self.taskPath = kwargs.get('taskPath', None)
        self.tgtFileConvictedBy = kwargs.get('tgtFileConvictedBy', None)
        self.tgtFileCreatedAt = kwargs.get('tgtFileCreatedAt', None)
        self.tgtFileCreationCount = kwargs.get('tgtFileCreationCount', None)
        self.tgtFileDeletionCount = kwargs.get('tgtFileDeletionCount', None)
        self.tgtFileExtension = kwargs.get('tgtFileExtension', None)
        self.tgtFileId = kwargs.get('tgtFileId', None)
        self.tgtFileIsExecutable = kwargs.get('tgtFileIsExecutable', None)
        self.tgtFileIsSigned = kwargs.get('tgtFileIsSigned', None)
        self.tgtFileLocation = kwargs.get('tgtFileLocation', None)
        self.tgtFileMd5 = kwargs.get('tgtFileMd5', None)
        self.tgtFileModificationCount = kwargs.get('tgtFileModificationCount', None)
        self.tgtFileModifiedAt = kwargs.get('tgtFileModifiedAt', None)
        self.tgtFileOldMd5 = kwargs.get('tgtFileOldMd5', None)
        self.tgtFileOldPath = kwargs.get('tgtFileOldPath', None)
        self.tgtFileOldSha1 = kwargs.get('tgtFileOldSha1', None)
        self.tgtFileOldSha256 = kwargs.get('tgtFileOldSha256', None)
        self.tgtFilePath = kwargs.get('tgtFilePath', None)
        self.tgtFileSha1 = kwargs.get('tgtFileSha1', None)
        self.tgtFileSha256 = kwargs.get('tgtFileSha256', None)
        self.tgtFileSize = kwargs.get('tgtFileSize', None)
        self.tgtPid = kwargs.get('tgtPid', None)
        self.tgtProcAccessRights = kwargs.get('tgtProcAccessRights', None)
        self.tgtProcActiveContentFileId = kwargs.get('tgtProcActiveContentFileId', None)
        self.tgtProcActiveContentHash = kwargs.get('tgtProcActiveContentHash', None)
        self.tgtProcActiveContentPath = kwargs.get('tgtProcActiveContentPath', None)
        self.tgtProcActiveContentSignedStatus = kwargs.get('tgtProcActiveContentSignedStatus', None)
        self.tgtProcActiveContentType = kwargs.get('tgtProcActiveContentType', None)
        self.tgtProcBinaryisExecutable = kwargs.get('tgtProcBinaryisExecutable', None)
        self.tgtProcCmdLine = kwargs.get('tgtProcCmdLine', None)
        self.tgtProcDisplayName = kwargs.get('tgtProcDisplayName', None)
        self.tgtProcImageMd5 = kwargs.get('tgtProcImageMd5', None)
        self.tgtProcImagePath = kwargs.get('tgtProcImagePath', None)
        self.tgtProcImageSha1 = kwargs.get('tgtProcImageSha1', None)
        self.tgtProcImageSha256 = kwargs.get('tgtProcImageSha256', None)
        self.tgtProcIntegrityLevel = kwargs.get('tgtProcIntegrityLevel', None)
        self.tgtProcisStorylineRoot = kwargs.get('tgtProcIsStorylineRoot', None)
        self.tgtProcIsRedirectCmdProcessor = kwargs.get('tgtProcIsRedirectCmdProcessor', None)
        self.tgtProcIsIsRedirectCmdProcessor = kwargs.get('tgtProcIsIsRedirectCmdProcessor', None)
        self.tgtProcIsNative64Bit = kwargs.get('tgtProcIsNative64Bit', None)
        self.tgtProcName = kwargs.get('tgtProcName', None)
        self.tgtProcPublisher = kwargs.get('tgtProcPublisher', None)
        self.tgtProcReasonSignatureInvalid = kwargs.get('tgtProcReasonSignatureInvalid', None)
        self.tgtProcRelation = kwargs.get('tgtProcRelation', None)
        self.tgtProcSessionId = kwargs.get('tgtProcSessionId', None)
        self.tgtProcSignedStatus = kwargs.get('tgtProcSignedStatus', None)
        self.tgtProcStartTime = kwargs.get('tgtProcStartTime', None)
        self.tgtProcStorylineId = kwargs.get('tgtProcStorylineId', None)
        self.tgtProcSubsystem = kwargs.get('tgtProcSubsystem', None)
        self.tgtProcUser = kwargs.get('tgtProcUser', None)
        self.tgtProcUid = kwargs.get('tgtProcUid', None)
        self.tgtProcVerifiedStatus = kwargs.get('tgtProcVerifiedStatus', None)
        self.tid = kwargs.get('tid', None)
        self.trueContext = kwargs.get('trueContext', None)
        self.url = kwargs.get('url', None)
        self.urlAction = kwargs.get('urlAction', None)
        self.user = kwargs.get('user', None)
        self.verifiedStatus = kwargs.get('verifiedStatus', None)
        for key in kwargs.keys():
            if not hasattr(self, key):
                # logger.info(f'Please note that Event class has no {key} attribute in SDK. '
                #             f'Setting it for the current instance')
                setattr(self, key, kwargs.get(key))


class Process(object):
    def __init__(self, **kwargs):
        self.agentId = kwargs.get('agentId', None)
        self.agentIsActive = kwargs.get('agentIsActive', None)
        self.agentOs = kwargs.get('agentOs', None)
        self.agentTimestamp = kwargs.get('agentTimestamp', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.attributes = kwargs.get('attributes', None)
        self.childProcImageMd5s = kwargs.get('childProcImageMd5s', None)
        self.childProcImagePaths = kwargs.get('childProcImagePaths', None)
        self.childProcImageSha1s = kwargs.get('childProcImageSha1s', None)
        self.childProcImageSha256s = kwargs.get('childProcImageSha256s', None)
        self.childProcNames = kwargs.get('childProcNames', None)
        self.containerId = kwargs.get('containerId', None)
        self.containerImage = kwargs.get('containerImage', None)
        self.containerLabels = kwargs.get('containerLabels', None)
        self.containerName = kwargs.get('containerName', None)
        self.dnsrequests = kwargs.get('dnsrequests', None)
        self.endpointMachineType = kwargs.get('endpointMachineType', None)
        self.endpointName = kwargs.get('endpointName', None)
        self.endpointOs = kwargs.get('endpointOs', None)
        self.endpointUuid = kwargs.get('endpointUuid', None)
        self.id = kwargs.get('id', None)
        self.indicatorCategories = kwargs.get('indicatorCategories', None)
        self.ips = kwargs.get('ips', None)
        self.isInfected = kwargs.get('isInfected', None)
        self.k8sClusterName = kwargs.get('k8sClusterName', None)
        self.k8sControllerLabels = kwargs.get('k8sControllerLabels', None)
        self.k8sControllerName = kwargs.get('k8sControllerName', None)
        self.k8sControllerType = kwargs.get('k8sControllerType', None)
        self.k8sNamespace = kwargs.get('k8sNamespace', None)
        self.k8sNamespaceLabels = kwargs.get('k8sNamespaceLabels', None)
        self.k8sNode = kwargs.get('k8sNode', None)
        self.k8sPodLabels = kwargs.get('k8sPodLabels', None)
        self.k8sPodName = kwargs.get('k8sPodName', None)
        self.moduleMd5s = kwargs.get('moduleMd5s', None)
        self.modulePaths = kwargs.get('modulePaths', None)
        self.moduleSha1s = kwargs.get('moduleSha1s', None)
        self.registryKeyPaths = kwargs.get('registryKeyPaths', None)
        self.siteId = kwargs.get('siteId', None)
        self.siteName = kwargs.get('siteName', None)
        self.srcProcActiveContentFileId = kwargs.get('srcProcActiveContentFileId', None)
        self.srcProcActiveContentHash = kwargs.get('srcProcActiveContentHash', None)
        self.srcProcActiveContentPath = kwargs.get('srcProcActiveContentPath', None)
        self.srcProcActiveContentSignedStatus = kwargs.get('srcProcActiveContentSignedStatus', None)
        self.srcProcActiveContentType = kwargs.get('srcProcActiveContentType', None)
        self.srcProcBinaryisExecutable = kwargs.get('srcProcBinaryisExecutable', None)
        self.srcProcCmdLine = kwargs.get('srcProcCmdLine', None)
        self.srcProcDisplayName = kwargs.get('srcProcDisplayName', None)
        self.srcProcImageMd5 = kwargs.get('srcProcImageMd5', None)
        self.srcProcImagePath = kwargs.get('srcProcImagePath', None)
        self.srcProcImageSha1 = kwargs.get('srcProcImageSha1', None)
        self.srcProcImageSha256 = kwargs.get('srcProcImageSha256', None)
        self.srcProcIntegrityLevel = kwargs.get('srcProcIntegrityLevel', None)
        self.srcProcIsStorylineRoot = kwargs.get('srcProcIsStorylineRoot', None)
        self.srcProcIsNative64Bit = kwargs.get('srcProcIsNative64Bit', None)
        self.srcProcIsRedirectCmdProcessor = kwargs.get('srcProcIsRedirectCmdProcessor', None)
        self.srcProcName = kwargs.get('srcProcName', None)
        self.srcProcParentImageMd5 = kwargs.get('srcProcParentImageMd5', None)
        self.srcProcParentImagePath = kwargs.get('srcProcParentImagePath', None)
        self.srcProcParentImageSha1 = kwargs.get('srcProcParentImageSha1', None)
        self.srcProcParentImageSha256 = kwargs.get('srcProcParentImageSha256', None)
        self.srcProcParentName = kwargs.get('srcProcParentName', None)
        self.srcProcParentPid = kwargs.get('srcProcParentPid', None)
        self.srcProcParentProcUid = kwargs.get('srcProcParentProcUid', None)
        self.srcProcParentStartTime = kwargs.get('srcProcParentStartTime', None)
        self.srcProcPid = kwargs.get('srcProcPid', None)
        self.srcProcPublisher = kwargs.get('srcProcPublisher', None)
        self.srcProcReasonSignatureInvalid = kwargs.get('srcProcReasonSignatureInvalid', None)
        self.srcProcRelatedToThreat = kwargs.get('srcProcRelatedToThreat', None)
        self.srcProcRpid = kwargs.get('srcProcRpid', None)
        self.srcProcSessionId = kwargs.get('srcProcSessionId', None)
        self.srcProcStartTime = kwargs.get('srcProcStartTime', None)
        self.srcProcStorylineId = kwargs.get('srcProcStorylineId', None)
        self.srcProcSubsystem = kwargs.get('srcProcSubsystem', None)
        self.srcProcTid = kwargs.get('srcProcTid', None)
        self.srcProcUser = kwargs.get('srcProcUser', None)
        self.srcProcUid = kwargs.get('srcProcUid', None)
        self.taskNames = kwargs.get('taskNames', None)
        self.tgtFileExtensions = kwargs.get('tgtFileExtensions', None)
        self.tgtFileMd5s = kwargs.get('tgtFileMd5s', None)
        self.tgtFilePaths = kwargs.get('tgtFilePaths', None)
        self.tgtFileSha1s = kwargs.get('tgtFileSha1s', None)
        self.tgtFileSha256s = kwargs.get('tgtFileSha256s', None)
        self.tgtProcImageMd5s = kwargs.get('tgtProcImageMd5s', None)
        self.tgtProcImagePaths = kwargs.get('tgtProcImagePaths', None)
        self.tgtProcImageSha1s = kwargs.get('tgtProcImageSha1s', None)
        self.tgtProcImageSha256s = kwargs.get('tgtProcImageSha256s', None)
        self.tgtProcNames = kwargs.get('tgtProcNames', None)
        self.urlActions = kwargs.get('urlActions', None)
        self.urls = kwargs.get('urls', None)
        for key in kwargs.keys():
            if not hasattr(self, key):
                # logger.info(f'Please note that Process class has no {key} attribute in SDK. '
                #             f'Setting it for the current instance')
                setattr(self, key, kwargs.get(key))


class StarAlert(object):
    def __init__(self, **kwargs):
        self.agentDetectionInfo = AgentDetectionInfo(**kwargs.get('agentDetectionInfo', {}))
        self.alertInfo = AlertInfo(**kwargs.get('alertInfo', {}))
        self.containerInfo = ContainerInfo(**kwargs.get('containerInfo', {}))
        self.kubernetesInfo = KubernetesInfo(**kwargs.get('kubernetesInfo', {}))
        self.ruleInfo = RuleInfo(**kwargs.get('ruleInfo', {}))
        self.sourceParentProcessInfo = SourceParentProcessInfo(**kwargs.get('sourceParentProcessInfo', {}))
        self.sourceProcessInfo = SourceProcessInfo(**kwargs.get('sourceProcessInfo', {}))
        self.agentRealtimeInfo = AgentRealtimeInfo(**kwargs.get('agentRealtimeInfo', {}))
        self.targetProcessInfo = TargetProcessInfo(**kwargs.get('targetProcessInfo', {}))


class TargetProcessInfo:
    def __init__(self, **kwargs):
        self.tgtFileCreatedAt = kwargs.get('tgtFileCreatedAt')
        self.tgtFileHashSha1 = kwargs.get('tgtFileHashSha1')
        self.tgtFileHashSha256 = kwargs.get('tgtFileHashSha256')
        self.tgtFileId = kwargs.get('tgtFileId')
        self.tgtFileIsSigned = kwargs.get('tgtFileIsSigned')
        self.tgtFileModifiedAt = kwargs.get('tgtFileModifiedAt')
        self.tgtFileOldPath = kwargs.get('tgtFileOldPath')
        self.tgtFilePath = kwargs.get('tgtFilePath')
        self.tgtProcCmdLine = kwargs.get('tgtProcCmdLine')
        self.tgtProcImagePath = kwargs.get('tgtProcImagePath')
        self.tgtProcIntegrityLevel = kwargs.get('tgtProcIntegrityLevel')
        self.tgtProcName = kwargs.get('tgtProcName')
        self.tgtProcPid = kwargs.get('tgtProcPid')
        self.tgtProcSignedStatus = kwargs.get('tgtProcSignedStatus')
        self.tgtProcStorylineId = kwargs.get('tgtProcStorylineId')
        self.tgtProcUid = kwargs.get('tgtProcUid')
        self.tgtProcessStartTime = kwargs.get('tgtProcessStartTime')




class AgentDetectionInfo(object):
    def __init__(self, **kwargs):
        self.machineType = kwargs.get('machineType')
        self.name = kwargs.get('name')
        self.osFamily = kwargs.get('osFamily')
        self.osName = kwargs.get('osName')
        self.osRevision = kwargs.get('osRevision')
        self.siteId = kwargs.get('siteId')
        self.uuid = kwargs.get('uuid')
        self.version = kwargs.get('version')


class AlertInfo(object):
    def __init__(self, **kwargs):
        self.alertId = kwargs.get('alertId')
        self.analystVerdict = kwargs.get('analystVerdict')
        self.createdAt = kwargs.get('createdAt')
        self.dvEventId = kwargs.get('dvEventId')
        self.hitType = kwargs.get('hitType')
        self.incidentStatus = kwargs.get('incidentStatus')
        self.reportedAt = kwargs.get('reportedAt')
        self.source = kwargs.get('source')
        self.dnsRequest = kwargs.get('dnsRequest')
        self.dnsResponse = kwargs.get('dnsResponse')
        self.dstIp = kwargs.get('dstIp')
        self.dstPort = kwargs.get('dstPort')
        self.eventType = kwargs.get('eventType')
        self.incidentStatus = kwargs.get('incidentStatus')
        self.indicatorCategory = kwargs.get('indicatorCategory')
        self.indicatorDescription = kwargs.get('indicatorDescription')
        self.indicatorName = kwargs.get('indicatorName')
        self.loginAccountDomain = kwargs.get('loginAccountDomain')
        self.loginAccountSid = kwargs.get('loginAccountSid')
        self.loginIsAdministratorEquivalent = kwargs.get('loginIsAdministratorEquivalent')
        self.loginIsSuccessful = kwargs.get('loginIsSuccessful')
        self.loginType = kwargs.get('loginType')
        self.loginsUserName = kwargs.get('loginsUserName')
        self.modulePath = kwargs.get('modulePath')
        self.moduleSha1 = kwargs.get('moduleSha1')
        self.netEventDirection = kwargs.get('netEventDirection')
        self.registryKeyPath = kwargs.get('registryKeyPath')
        self.registryOldValue = kwargs.get('registryOldValue')
        self.registryOldValueType = kwargs.get('registryOldValueType')
        self.registryPath = kwargs.get('registryPath')
        self.registryValue = kwargs.get('registryValue')
        self.reportedAt = kwargs.get('reportedAt')
        self.srcIp = kwargs.get('srcIp')
        self.srcPort = kwargs.get('srcPort')
        self.srcMachineIp = kwargs.get('srcMachineIp')
        self.tiIndicatorComparisonMethod = kwargs.get('tiIndicatorComparisonMethod')
        self.tiIndicatorSource = kwargs.get('tiIndicatorSource')
        self.tiIndicatorType = kwargs.get('tiIndicatorType')
        self.tiIndicatorValue = kwargs.get('tiIndicatorValue')
        self.updatedAt = kwargs.get('updatedAt')


class ContainerInfo(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.image = kwargs.get('image')
        self.labels = kwargs.get('labels')
        self.name = kwargs.get('name')


class KubernetesInfo(object):
    def __init__(self, **kwargs):
        self.cluster = kwargs.get('cluster')
        self.controllerKind = kwargs.get('controllerKind')
        self.controllerLabels = kwargs.get('controllerLabels')
        self.controllerName = kwargs.get('controllerName')
        self.namespace = kwargs.get('namespace')
        self.namespaceLabels = kwargs.get('namespaceLabels')
        self.node = kwargs.get('node')
        self.pod = kwargs.get('pod')
        self.podLabels = kwargs.get('podLabels')


class RuleInfo(object):
    def __init__(self, **kwargs):
        self.description = kwargs.get('description')
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.scopeLevel = kwargs.get('scopeLevel')
        self.severity = kwargs.get('severity')
        self.treatAsThreat = kwargs.get('treatAsThreat')


class SourceParentProcessInfo(object):
    def __init__(self, **kwargs):
        self.commandline = kwargs.get('commandline')
        self.fileHashMd5 = kwargs.get('fileHashMd5')
        self.fileHashSha1 = kwargs.get('fileHashSha1')
        self.fileHashSha256 = kwargs.get('fileHashSha256')
        self.filePath = kwargs.get('filePath')
        self.fileSignerIdentity = kwargs.get('fileSignerIdentity')
        self.integrityLevel = kwargs.get('integrityLevel')
        self.name = kwargs.get('name')
        self.pid = kwargs.get('pid')
        self.pidStarttime = kwargs.get('pidStarttime')
        self.storyline = kwargs.get('storyline')
        self.subsystem = kwargs.get('subsystem')
        self.uniqueId = kwargs.get('uniqueId')
        self.user = kwargs.get('user')


class SourceProcessInfo(object):
    def __init__(self, **kwargs):
        self.commandline = kwargs.get('commandline')
        self.fileHashMd5 = kwargs.get('fileHashMd5')
        self.fileHashSha1 = kwargs.get('fileHashSha1')
        self.fileHashSha256 = kwargs.get('fileHashSha256')
        self.filePath = kwargs.get('filePath')
        self.fileSignerIdentity = kwargs.get('fileSignerIdentity')
        self.integrityLevel = kwargs.get('integrityLevel')
        self.name = kwargs.get('name')
        self.pid = kwargs.get('pid')
        self.pidStarttime = kwargs.get('pidStarttime')
        self.storyline = kwargs.get('storyline')
        self.subsystem = kwargs.get('subsystem')
        self.uniqueId = kwargs.get('uniqueId')
        self.user = kwargs.get('user')


class AgentRealtimeInfo(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.os = kwargs.get('os')
        self.machineType = kwargs.get('machineType')
        self.isDecommissioned = kwargs.get('isDecommissioned')
        self.isActive = kwargs.get('isActive')
        self.infected = kwargs.get('infected')
        self.id = kwargs.get('id')
        self.uuid = kwargs.get('uuid')
