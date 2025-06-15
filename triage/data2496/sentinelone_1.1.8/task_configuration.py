

class TaskConfiguration(object):

    def __init__(self, **kwargs):
        self.concurrencyConfigUpdatedAt = kwargs.get('concurrencyConfigUpdatedAt', None)
        self.concurrencyConfigUpdatedBy = kwargs.get('concurrencyConfigUpdatedBy', None)
        self.inheritParentConcurrencyConfig = kwargs.get('inheritParentConcurrencyConfig', None)
        self.inheritParentMaintenanceConfig = kwargs.get('inheritParentMaintenanceConfig', None)
        self.maintenanceConfigUpdatedAt = kwargs.get('maintenanceConfigUpdatedAt', None)
        self.maintenanceConfigUpdatedBy = kwargs.get('maintenanceConfigUpdatedBy', None)
        self.maintenanceWindowsByDay = kwargs.get('maintenanceWindowsByDay', None)
        self.maxConcurrent = kwargs.get('maxConcurrent', None)
        self.parentMaxConcurrent = kwargs.get('parentMaxConcurrent', None)
        self.taskType = kwargs.get('taskType', None)
        self.timezoneGmt = kwargs.get('timezoneGmt', None)
