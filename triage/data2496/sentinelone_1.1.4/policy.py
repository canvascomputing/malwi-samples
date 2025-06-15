import six


class Engines(object):
    def __init__(self, **kwargs):
        self.applicationControl = kwargs.get('applicationControl', None)
        self.dataFiles = kwargs.get('dataFiles', None)
        self.executables = kwargs.get('executables', None)
        self.exploits = kwargs.get('exploits', None)
        self.lateralMovement = kwargs.get('lateralMovement', None)
        self.penetration = kwargs.get('penetration', None)
        self.preExecution = kwargs.get('preExecution', None)
        self.preExecutionSuspicious = kwargs.get('preExecutionSuspicious', None)
        self.pup = kwargs.get('pup', None)
        self.remoteShell = kwargs.get('remoteShell', None)
        self.reputation = kwargs.get('reputation', None)


class IocAttributes(object):
    def __init__(self, **kwargs):
        self.autoInstallBrowserExtensions = kwargs.get('autoInstallBrowserExtensions', None)
        self.behavioralIndicators = kwargs.get('behavioralIndicators', None)
        self.commandScripts = kwargs.get('commandScripts', None)
        self.crossProcess = kwargs.get('crossProcess', None)
        self.dataMasking = kwargs.get('dataMasking', None)
        self.dllModuleLoad = kwargs.get('dllModuleLoad', None)
        self.dns = kwargs.get('dns', None)
        self.fds = kwargs.get('fds', None)
        self.file = kwargs.get('file', None)
        if kwargs.get('headers', None):
            self.headers = kwargs.get('headers', None)
        self.fullDiskScan = kwargs.get('fullDiskScan', None)
        self.ip = kwargs.get('ip', None)
        self.login = kwargs.get('login', None)
        self.process = kwargs.get('process', None)
        self.registry = kwargs.get('registry', None)
        self.scheduledTask = kwargs.get('scheduledTask', None)
        self.url = kwargs.get('url', None)
        self.namedPipe = kwargs.get('namedPipe', None)
        self.namedPipeExtended = kwargs.get('namedPipeExtended', None)


class AutoFileUpload(object):
    def __init__(self, **kwargs):
        self.enabled = kwargs.get('enabled', None)
        self.includeBenignFiles = kwargs.get('includeBenignFiles', None)
        self.maxDailyFileUpload = kwargs.get('maxDailyFileUpload', None)
        self.maxDailyFileUploadLimit = kwargs.get('maxDailyFileUploadLimit', None)
        self.maxFileSize = kwargs.get('maxFileSize', None)
        self.maxFileSizeLimit = kwargs.get('maxFileSizeLimit', None)
        self.maxLocalDiskUsage = kwargs.get('maxLocalDiskUsage', None)
        self.maxLocalDiskUsageLimit = kwargs.get('maxLocalDiskUsageLimit', None)


class AgentUiConfig(object):
    def __init__(self, **kwargs):
        self.agentUiOn = kwargs.get('agentUiOn', None)
        self.threatPopUpNotifications = kwargs.get('threatPopUpNotifications', None)
        self.devicePopUpNotifications = kwargs.get('devicePopUpNotifications', None)
        self.showSuspicious = kwargs.get('showSuspicious', None)
        self.showAgentWarnings = kwargs.get('showAgentWarnings', None)
        self.showDeviceTab = kwargs.get('showDeviceTab', None)
        self.showQuarantineTab = kwargs.get('showQuarantineTab', None)
        self.showSupport = kwargs.get('showSupport', None)
        self.maxEventAgeDays = kwargs.get('maxEventAgeDays', None)
        self.contactFreeText = kwargs.get('contactFreeText', None)
        self.contactCompany = kwargs.get('contactCompany', None)
        self.contactEmail = kwargs.get('contactEmail', None)
        self.contactPhoneNumber = kwargs.get('contactPhoneNumber', None)
        self.contactDirectMessage = kwargs.get('contactDirectMessage', None)
        self.contactSupportWebsite = kwargs.get('contactSupportWebsite', None)
        self.contactOther = kwargs.get('contactOther', None)


class RemoteScriptOrchestration(object):
    def __init__(self, **kwargs):
        self.alwaysUploadStreamToCloud = kwargs.get('alwaysUploadStreamToCloud', None)
        self.maxDailyFileUpload = kwargs.get('maxDailyFileUpload', None)
        self.maxDailyFileUploadLimit = kwargs.get('maxDailyFileUploadLimit', None)
        self.maxFileSize = kwargs.get('maxFileSize', None)
        self.maxFileSizeLimit = kwargs.get('maxFileSizeLimit', None)

    def to_json(self):
        return {k: v for (k, v) in self.__dict__.items() if v is not None}


class Policy(object):
    def __init__(self, **kwargs):
        self.agentLoggingOn = kwargs.get('agentLoggingOn', None)
        self.agentNotification = kwargs.get('agentNotification', None)
        self.antiTamperingOn = kwargs.get('antiTamperingOn', None)
        self.agentUi = kwargs.get('agentUi', None)
        self.agentUiOn = kwargs.get('agentUiOn', None)
        self.allowRemoteShell = kwargs.get('allowRemoteShell', None)
        self.autoDecommissionDays = kwargs.get('autoDecommissionDays', None)
        self.autoDecommissionOn = kwargs.get('autoDecommissionOn', None)
        self.autoImmuneOn = kwargs.get('autoImmuneOn', None)
        self.autoMitigationAction = kwargs.get('autoMitigationAction', None)
        self.cloudValidationOn = kwargs.get('cloudValidationOn', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.engines = kwargs.get('engines', None)
        self.remoteScriptOrchestration = kwargs.get('remoteScriptOrchestration', None)
        self.dvAttributesPerEventType = kwargs.get('dvAttributesPerEventType', None)
        self.isDvPolicyPerEventType = kwargs.get('isDvPolicyPerEventType', None)
        self.iocAttributes = kwargs.get('iocAttributes', None)

        if isinstance(self.iocAttributes, dict):
            self.iocAttributes = IocAttributes(**self.iocAttributes)
        
        if isinstance(self.engines, dict):
            self.engines = Engines(**self.engines)

        if kwargs.get('autoFileUpload', None):
            self.autoFileUpload = kwargs.get('autoFileUpload', AutoFileUpload())
            if isinstance(self.autoFileUpload, dict):
                self.autoFileUpload = AutoFileUpload(**self.autoFileUpload)
        else:
            self.autoFileUpload = None

        if kwargs.get('agentUi', None):
            self.agentUi = kwargs.get('agentUi', AgentUiConfig())
            if isinstance(self.agentUi, dict):
                self.agentUi = AgentUiConfig(**self.agentUi)
        else:
            self.agentUi = None

        if isinstance(self.remoteScriptOrchestration, dict):
            self.remoteScriptOrchestration = RemoteScriptOrchestration(**self.remoteScriptOrchestration)

        self.inheritedFrom = kwargs.get('inheritedFrom', None)
        self.isDefault = kwargs.get('isDefault', None)
        self.ioc = kwargs.get('ioc', None)
        self.iocSupported = kwargs.get('iocSupported', None)
        self.mitigationMode = kwargs.get('mitigationMode', None)
        self.mitigationModeSuspicious = kwargs.get('mitigationModeSuspicious', None)
        self.monitorOnExecute = kwargs.get('monitorOnExecute', None)
        self.monitorOnWrite = kwargs.get('monitorOnWrite', None)
        self.networkQuarantineOn = kwargs.get('networkQuarantineOn', None)
        self.rememberLastLocation = kwargs.get('rememberLastLocation', None)
        self.researchOn = kwargs.get('researchOn', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.userFullName = kwargs.get('userFullName', None)
        self.userId = kwargs.get('userId', None)
        self.snapshotsOn = kwargs.get('snapshotsOn', None)
        self.scanNewAgents = kwargs.get('scanNewAgents', None)
        self.fwForNetworkQuarantineEnabled = kwargs.get('fwForNetworkQuarantineEnabled', None)

    def to_json(self):
        orig_json = self.__dict__
        for key in list(orig_json):
            if key in ['createdAt', 'updatedAt']:
                del orig_json[key]
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        engines = self.engines
        if not isinstance(self.engines, dict):
            engines = self.engines.__dict__
        non_empty_engines = {k: v for (k, v) in six.iteritems(engines) if v is not None}
        if self.iocAttributes:
            ioc_attrs = self.iocAttributes
            if not isinstance(self.iocAttributes, dict):
                ioc_attrs = self.iocAttributes.__dict__
            non_empty_ioc_attrs = {k: v for (k, v) in six.iteritems(ioc_attrs) if v is not None}
            non_empty_json['iocAttributes'] = non_empty_ioc_attrs
        if self.autoFileUpload:
            upl_attrs = self.autoFileUpload
            if not isinstance(self.autoFileUpload, dict):
                upl_attrs = self.autoFileUpload.__dict__
            non_empty_upl_attrs = {k: v for (k, v) in six.iteritems(upl_attrs) if v is not None}
            non_empty_json['autoFileUpload'] = non_empty_upl_attrs
        if self.agentUi:
            agent_ui_attrs = self.agentUi
            if not isinstance(self.agentUi, dict):
                agent_ui_attrs = self.agentUi.__dict__
            non_empty_agent_ui_attrs = {k: v for (k, v) in six.iteritems(agent_ui_attrs) if v is not None}
            non_empty_json['agentUi'] = non_empty_agent_ui_attrs

        if self.remoteScriptOrchestration:
            remote_script_orchestration_attrs = self.remoteScriptOrchestration
            if not isinstance(self.remoteScriptOrchestration, dict):
                remote_script_orchestration_attrs = self.remoteScriptOrchestration.__dict__
            non_empty_remote_script_orchestration_attrs = {k: v for (k, v) in
                                                           six.iteritems(remote_script_orchestration_attrs) if
                                                           v is not None}
            non_empty_json['remoteScriptOrchestration'] = non_empty_remote_script_orchestration_attrs

        non_empty_json['engines'] = non_empty_engines
        return non_empty_json
