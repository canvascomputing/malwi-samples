
class NavigationObj(object):
    def __init__(self, **kwargs):
        self.ancestors = kwargs.get('ancestors', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.scope = kwargs.get('scope', None)
        self.state = kwargs.get('state', None)
        self.totalChildren = kwargs.get('totalChildren', None)
        self.totalEndpoints = kwargs.get('totalEndpoints', None)
        self.type = kwargs.get('type', None)
