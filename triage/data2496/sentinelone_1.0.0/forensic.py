class ApplicationForensicDetails(object):
    def __init__(self, **kwargs):
        self.agent = kwargs.get('agent', None)
        self.applicationCreated = kwargs.get('application_created', None)
        self.applicationId = kwargs.get('application_id', None)
        self.fetchStoryStatus = kwargs.get('fetch_story_status', None)
        if kwargs.get('file', None):
            self.file = ApplicationForensicsFile(**kwargs.get('file'))
        else:
            self.file = None
        if kwargs.get('process', None):
            self.process = ApplicationForensicsProcess(**kwargs.get('process'))
        else:
            self.process = None
        self.processCreatedAt = kwargs.get('process_created_at', None)
        self.processDisplayName = kwargs.get('process_display_name', None)
        self.seenOnNetwork = kwargs.get('seen_on_network', None)


class ApplicationForensicsFile(object):
    def __init__(self, **kwargs):
        self.contentHash = kwargs.get('content_hash', None)
        self.createdDate = kwargs.get('created_date', None)
        self.displayName = kwargs.get('display_name', None)
        self.isSystem = kwargs.get('is_system', None)
        self.objectId = kwargs.get('object_id', None)
        self.path = kwargs.get('path', None)
        self.permission = kwargs.get('permission', None)
        self.size = kwargs.get('size', None)


class ApplicationForensicsProcess(object):
    def __init__(self, **kwargs):
        self.bundleId = kwargs.get('bundle_id', None)
        self.createdDate = kwargs.get('created_date', None)
        self.displayName = kwargs.get('display_name', None)
        self.executableFileId = kwargs.get('executable_file_id', None)
        self.isPrimary = kwargs.get('is_primary', None)
        self.isRoot = kwargs.get('is_root', None)
        self.objectId = kwargs.get('object_id', None)
        self.pid = kwargs.get('pid', None)


class ThreatForensicDetails(object):
    def __init__(self, **kwargs):
        self.agent = kwargs.get('agent', None)
        self.agentVersion = kwargs.get('agent_version', None)
        self.categoryScores = kwargs.get('category_scores', None)
        self.certId = kwargs.get('cert_id', None)
        self.fileCreatedAt = kwargs.get('file_created_at', None)
        self.fileDisplayName = kwargs.get('file_display_name', None)
        self.fileHash = kwargs.get('file_hash', None)
        self.graph = kwargs.get('graph', None)
        self.indicators = kwargs.get('indicators', None)
        self.isCertValid = kwargs.get('', None)
        self.occurredAt = kwargs.get('occurred_at', None)
        self.policyId = kwargs.get('policy_id', None)
        self.publisher = kwargs.get('publisher', None)
        self.rawData = kwargs.get('raw_data', None)  # dict {"edges = [],"nodes = {}}
        self.resolved = kwargs.get('resolved', None)
        self.summary = kwargs.get('summary', None)  # list
        # dict {
        #   "file = {"create = 0,"delete = 0,"write = 0},
        #   "network = {"connections = 0,"dns = 0},
        #   "registry = {"persistence = 0,"security = 0,"stealth = 0}
        # }
        self.summaryOverview = kwargs.get('summary_overview', None)
        self.threatCreated = kwargs.get('threat_created', None)
        self.threatDuration = kwargs.get('threat_duration', None)
        self.threatId = kwargs.get('threat_id', None)
        self.username = kwargs.get('username', None)


class ThreatForensics(object):
    def __init__(self, **kwargs):
        self.classifierName = kwargs.get('classifier_name', None)
        self.mitigationStatus = kwargs.get('mitigation_status', None)
        self.classification = kwargs.get('classification', None)
        self.fromScan = kwargs.get('from_scan', None)
        self.initiatedBy = kwargs.get('initiated_by', None)
        self.occurred_at = kwargs.get('occurred_at', None)
        self.inQuarantine = kwargs.get('in_quarantine', None)
        self.agent = kwargs.get('agent', None)
        self.threat_created = kwargs.get('threat_created', None)
        self.fileHash = kwargs.get('file_hash', None)
        self.fileCreated_at = kwargs.get('file_created_at', None)
        self.annotationUrl = kwargs.get('annotation_url', None)
        self.classificationSource = kwargs.get('classification_source', None)
        self.mitigationActions = kwargs.get('mitigation_actions', None)
        self.resolved = kwargs.get('resolved', None),
        self.annotation = kwargs.get('annotation', None)
        self.threat_id = kwargs.get('threat_id', None)
        self.filePath = kwargs.get('file_path', None)
        self.seenOnNetwork = kwargs.get('seen_on_network', None)
        self.mitigationReport = kwargs.get('mitigation_report', None)
        self.fileDescription = kwargs.get('file_description', None)
        self.fileContentHash = kwargs.get('file_content_hash', None)
        self.whitening_options = kwargs.get('whitening_options', None)
        self.malicious_process_arguments = kwargs.get('malicious_process_arguments', None)
        self.file_display_name = kwargs.get('file_display_name', None)
        self.malicious_group_id = kwargs.get('malicious_group_id', None)
        self.marked_as_benign = kwargs.get('marked_as_benign', None)


class ApplicationForensics(object):
    def __init__(self, **kwargs):
        self.agent = kwargs.get('agent', None)
        self.application_created = kwargs.get('application_created', None)
        self.application_id = kwargs.get('application_id', None)
        self.fetch_story_status = kwargs.get('fetch_story_status', None)
        if kwargs.get('file', None):
            self.file = ApplicationForensicsFile(**kwargs.get('file'))
        else:
            self.file = None
        if kwargs.get('process', None):
            self.process = ApplicationForensicsProcess(**kwargs.get('process'))
            self.malicious_process_arguments = kwargs.get('malicious_process_arguments', None)
        else:
            self.process = None
            self.malicious_process_arguments = None
        self.process_created_at = kwargs.get('process_created_at', None)
        self.process_display_name = kwargs.get('process_display_name', None)
        self.seen_on_network = kwargs.get('seen_on_network', None)


class ThreatSeenOnNetwork(object):
    def __init__(self, **kwargs):
        self.agent = kwargs.get('agent', None)
        self.agent_version = kwargs.get('agent_version', None)
        self.created_date = kwargs.get('created_date', None)
        self.from_cloud = kwargs.get('from_cloud', None)
        self.malicious_group_id = kwargs.get('malicious_group_id', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.resolved = kwargs.get('resolved', None)
        self.status = kwargs.get('status', None)
