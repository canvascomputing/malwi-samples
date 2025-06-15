import six


class InstalledApplication(object):

    def __init__(self, **kwargs):
        self.agentComputerName = kwargs.get('agentComputerName', None)
        self.agentDomain = kwargs.get('agentDomain', None)
        self.agentId = kwargs.get('agentId', None)
        self.agentInfected = kwargs.get('agentInfected', None)
        self.agentIsActive = kwargs.get('agentIsActive', None)
        self.agentIsDecommissioned = kwargs.get('agentIsDecommissioned', None)
        self.agentMachineType = kwargs.get('agentMachineType', None)
        self.agentNetworkStatus = kwargs.get('agentNetworkStatus', None)
        self.agentOsType = kwargs.get('agentOsType', None)
        self.agentUuid = kwargs.get('agentUuid', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.id = kwargs.get('id', None)
        self.installedAt = kwargs.get('installedAt', None)
        self.name = kwargs.get('name', None)
        self.osType = kwargs.get('osType', None)
        self.publisher = kwargs.get('publisher', None)
        self.riskLevel = kwargs.get('riskLevel', None)
        self.signed = kwargs.get('signed', None)
        self.size = kwargs.get('size', None)
        self.type = kwargs.get('type', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.version = kwargs.get('version', None)

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class CveEnriched(InstalledApplication):
    def __init__(self, **kwargs):
        super(CveEnriched, self).__init__(**kwargs)
        self.cves = None
        cves = kwargs.get('cves', None)
        if cves:
            cves_list = list()
            for cve in cves:
                cves_list.append(Cve(**cve))
            self.cves = cves_list


class Cve(object):

    def __init__(self, **kwargs):
        self.score = kwargs.get('score', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.cveId = kwargs.get('cveId', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.link = kwargs.get('link', None)
        self.riskLevel = kwargs.get('riskLevel', None)
        self.publishedAt = kwargs.get('publishedAt', None)
        self.updatedAt = kwargs.get('updatedAt', None)

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json
