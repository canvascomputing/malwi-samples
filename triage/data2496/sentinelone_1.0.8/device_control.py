import six


class Rule(object):

    def __init__(self, **kwargs):
        self.order = kwargs.get('order', None)
        self.interface = kwargs.get('interface', None)
        self.deviceClass = kwargs.get('deviceClass', None)
        self.deviceClassName = kwargs.get('deviceClassName', None)
        self.serviceClass = kwargs.get('serviceClass', None)
        self.ruleName = kwargs.get('ruleName', None)
        self.vendorId = kwargs.get('vendorId', None)
        self.productId = kwargs.get('productId', None)
        self.action = kwargs.get('action', None)
        self.status = kwargs.get('status', None)
        self.scopeId = kwargs.get('scopeId', None)
        self.scopeLevel = kwargs.get('scopeLevel', None)
        self.uId = kwargs.get('uId', None)
        self.id = kwargs.get('id', None)
        self.ruleType = kwargs.get('ruleType', None)
        self.version = kwargs.get('version', None)
        self.minorClasses = kwargs.get('minorClasses', None)
        self.accessPermission = kwargs.get('accessPermission', None)
        self.bluetoothAddress = kwargs.get('bluetoothAddress', None)
        self.gattService = kwargs.get('gattService', None)
        self.deviceName = kwargs.get('deviceName', None)
        self.manufacturerName = kwargs.get('manufacturerName', None)
        self.deviceInformationServiceInfoKey = kwargs.get('deviceInformationServiceInfoKey', None)
        self.deviceInformationServiceInfoValue = kwargs.get('deviceInformationServiceInfoValue', None)

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json


class DeviceEvent(object):

    def __init__(self, **kwargs):
        self.eventId = kwargs.get('eventId', None)
        self.vendorId = kwargs.get('vendorId', None)
        self.eventTime = kwargs.get('eventTime', None)
        self.uId = kwargs.get('uId', None)
        self.deviceName = kwargs.get('deviceName', None)
        self.eventType = kwargs.get('eventType', None)
        self.serviceClass = kwargs.get('serviceClass', None)
        self.ruleId = kwargs.get('ruleId', None)
        self.deviceClass = kwargs.get('deviceClass', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.createdAt = kwargs.get('createdAt', None)
        self.interface = kwargs.get('interface', None)
        self.agentId = kwargs.get('agentId', None)
        self.id = kwargs.get('id', None)
        self.productId = kwargs.get('productId', None)
        self.bluetoothAddress = kwargs.get('bluetoothAddress', None)
        self.gattService = kwargs.get('gattService', None)
        self.manufacturerName = kwargs.get('manufacturerName', None)
        self.deviceInformationServiceInfoKey = kwargs.get('deviceInformationServiceInfoKey', None)
        self.deviceInformationServiceInfoValue = kwargs.get('deviceInformationServiceInfoValue', None)
        self.lmpVersion = kwargs.get('lmpVersion', None)
