class RemoteScriptPackage(object):
    def __init__(self, **kwargs):
        self.bucketName = kwargs.get('bucketName', None)
        self.endpointExpiration = kwargs.get('endpointExpiration', None)
        self.endpointExpirationSeconds = kwargs.get('endpointExpirationSeconds', None)
        self.fileName = kwargs.get('fileName', None)
        self.fileSize = kwargs.get('fileSize', None)
        self.id = kwargs.get('id', None)
        self.signature = kwargs.get('signature', None)
        self.signatureType = kwargs.get('signatureType', None)


class RemoteScript(object):
    def __init__(self, **kwargs):
        self.bucketName = kwargs.get('bucketName', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.createdByUser = kwargs.get('createdByUser', None)
        self.createdByUserId = kwargs.get('createdByUserId', None)
        self.creator = kwargs.get('creator', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.fileName = kwargs.get('fileName', None)
        self.fileSize = kwargs.get('fileSize', None)
        self.id = kwargs.get('id', None)
        self.inputExample = kwargs.get('inputExample', None)
        self.inputInstructions = kwargs.get('inputInstructions', None)
        self.inputRequired = kwargs.get('inputRequired', None)
        self.mgmtId = kwargs.get('mgmtId', None)
        self.osTypes = kwargs.get('osTypes', None)
        self.outputFilePaths = kwargs.get('outputFilePaths', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.scopeLevel = kwargs.get('scopeLevel', None)
        self.scriptName = kwargs.get('scriptName', None)
        self.scriptRuntimeTimeoutSeconds = kwargs.get('scriptRuntimeTimeoutSeconds', None)
        self.scriptType = kwargs.get('scriptType', None)
        self.shortFileName = kwargs.get('shortFileName', None)
        self.signature = kwargs.get('signature', None)
        self.signatureType = kwargs.get('signatureType', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.updater = kwargs.get('updater', None)
        self.updaterId = kwargs.get('updaterId', None)
        self.version = kwargs.get('version', None)
        self.scriptDescription = kwargs.get('scriptDescription', None)
        self.package = RemoteScriptPackage(**kwargs['package']) if 'package' in kwargs else None


class RemoteScriptsDownloadLink(object):
    def __init__(self, **kwargs):
        self.download_url = kwargs.get('downloadUrl', None)
        self.file_name = kwargs.get('fileName', None)
        self.task_id = kwargs.get('taskId', None)


class RemoteScriptsDownloadLinkError(object):
    def __init__(self, **kwargs):
        self.error_string = kwargs.get('errorString', None)
        self.task_id = kwargs.get('taskId', None)