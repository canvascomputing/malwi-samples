
class RiskDataTypes:
    VULN_DETAILS = 'vulnerabilityDetails'


class VulnDetails(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.cveId = kwargs.get('cveId')
        self.application = kwargs.get('application')
        self.applicationName = kwargs.get('applicationName')
        self.applicationVendor = kwargs.get('applicationVendor')
        self.applicationVersion = kwargs.get('applicationVersion')
        self.osType = kwargs.get('osType')
        self.endpointId = kwargs.get('endpointId')
        self.endpointName = kwargs.get('endpointName')
        self.endpointType = kwargs.get('endpointType')
        self.baseScore = kwargs.get('baseScore')
        self.cvssVersion = kwargs.get('cvssVersion')
        self.severity = kwargs.get('severity')
        self.daysDetected = kwargs.get('daysDetected')
        self.detectedDate = kwargs.get('detectedDate')
        self.publishedDate = kwargs.get('publishedDate')
        self.domain = kwargs.get('domain')
        self.installationPath = kwargs.get('installationPath')
        self.vulnerabilityDescription = kwargs.get('vulnerabilityDescription')
        self.mitreUrl = kwargs.get('mitreUrl')
        self.nvdUrl = kwargs.get('nvdUrl')
        self.accountName = kwargs.get('accountName')
        self.siteName = kwargs.get('siteName')
        self.groupName = kwargs.get('groupName')

    def __repr__(self):
        return f'<management.mgmtsdk_v2_1.entities.app_management.VulnDetails: {self.cveId}>'


def get_risk_data_class(**kwargs):
    data = kwargs
    if kwargs.get('type') == RiskDataTypes.VULN_DETAILS:
        data = VulnDetails(**kwargs.get('data'))
    return data
