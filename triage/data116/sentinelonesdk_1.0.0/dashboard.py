
class Dashboard(object):

    def __init__(self, **kwargs):
        self.agents = DashboardAgents(**kwargs.get('agents'))
        self.threats = DashboardThreats(**kwargs.get('threats'))


class DashboardAgents(object):
    def __init__(self, **kwargs):
        self.decommissioned = kwargs.get('decommissioned', None)
        self.infected = kwargs.get('infected', None)
        self.online = kwargs.get('online', None)
        self.outOfDate = kwargs.get('outOfDate', None)
        self.total = kwargs.get('total', None)
        self.upToDate = kwargs.get('upToDate', None)


class DashboardThreats(object):
    def __init__(self, **kwargs):
        self.notMitigated = kwargs.get('notMitigated', None)
        self.notMitigatedNotResolved = kwargs.get('notMitigatedNotResolved', None)
        self.notResolved = kwargs.get('notResolved', None)
        self.inProgress = kwargs.get('inProgress', None)
        self.resolved = kwargs.get('resolved', None)
        self.maliciousNotResolved = kwargs.get('maliciousNotResolved', None)
        self.suspiciousNotResolved = kwargs.get('suspiciousNotResolved', None)
        self.total = kwargs.get('total', None)
