class ApplicationCatalog(object):
    def __init__(self, **kwargs):
        self.appId = kwargs.get('appId', None)
        self.applicationName = kwargs.get('applicationName', None)
        self.inAppInventory = kwargs.get('inAppInventory', None)
        self.exclusionsStatus = kwargs.get('exclusionsStatus', None)
        if kwargs.get('exclusions', None):
            self.exclusions = []
            for exclusion in kwargs.get('exclusions'):
                self.exclusions.append(ApplicationExclusions(**exclusion))


class ApplicationExclusions(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)
        self.osType = kwargs.get('osType', None)
        self.description = kwargs.get('description', None)
        self.alreadyExcluded = kwargs.get('alreadyExcluded', None)
        if kwargs.get('attributes', None):
            self.attributes = []
            for attr in kwargs.get('attributes'):
                self.attributes.append(CatalogExclusionAttributes(**attr))


class CatalogExclusionAttributes(object):
    def __init__(self, **kwargs):
        self.display = kwargs.get('display', None)
        self.displayAttribute = kwargs.get('displayAttribute', True)
        self.fieldId = kwargs.get('fieldId', None)
        self.section = kwargs.get('section', None)
        self.value = kwargs.get('value', None)
