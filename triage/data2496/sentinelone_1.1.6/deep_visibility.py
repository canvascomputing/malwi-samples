from management.mgmtsdk_v2.entities.agent import Agent


class SeenOnNetwork(object):
    def __init__(self, **kwargs):
        self.firstSeen = kwargs.get('firstSeen', None)
        self.lastSeen = kwargs.get('lastSeen', None)

        
class Process(object):
    def __init__(self, **kwargs):
        self.agentTimestamp = kwargs.get('agentTimestamp', None)
        self.commandLine = kwargs.get('commandLine', None)
        self.groupId = kwargs.get('groupId', None)
        self.hasParent = kwargs.get('hasParent', None)
        self.id = kwargs.get('id', None)
        self.imagePath = kwargs.get('imagePath', None)
        self.imageSha1Hash = kwargs.get('imageSha1Hash', None)
        self.isMalicious = kwargs.get('isMalicious', None)
        self.name = kwargs.get('name', None)
        self.processStartTime = kwargs.get('processStartTime', None)
        self.processUniqueKey = kwargs.get('processUniqueKey', None)
        self.type = kwargs.get('type', None)


class AgentBreakdown(object):
    def __init__(self, **kwargs):
        agent = kwargs.get('agent', None)
        if agent is not None:
            self.agent = Agent(**agent)
        self.attach = kwargs.get('attach', None)
        self.detach = kwargs.get('detach', None)
        self.dnses = kwargs.get('dnses', None)
        self.example = kwargs.get('example', None)
        self.hashes = kwargs.get('hashes', None)
        self.headers = kwargs.get('headers', None)
        self.mount = kwargs.get('mount', None)
        self.processes = kwargs.get('processes', None)
        self.tcps = kwargs.get('tcps', None)
        self.urls = kwargs.get('urls', None)



class Event(object):
    def __init__(self, **kwargs):
        self.agentTimestamp = kwargs.get('agentTimestamp', None)
        self.commandLine = kwargs.get('commandLine', None)
        self.destIp = kwargs.get('destIp', None)
        self.destPort = kwargs.get('destPort', None)
        self.fullPath = kwargs.get('fullPath', None)
        self.groupId = kwargs.get('groupId', None)
        self.hasParent = kwargs.get('hasParent', None)
        self.id = kwargs.get('id', None)
        self.imagePath = kwargs.get('imagePath', None)
        self.imageSha1Hash = kwargs.get('imageSha1Hash', None)
        self.md5 = kwargs.get('md5', None)
        self.method = kwargs.get('method', None)
        self.name = kwargs.get('name', None)
        self.processStartTime = kwargs.get('processStartTime', None)
        self.processUniqueKey = kwargs.get('processUniqueKey', None)
        self.queryName = kwargs.get('queryName', None)
        self.queryResults = kwargs.get('queryResults', None)
        self.sha1 = kwargs.get('sha1', None)
        self.sha256 = kwargs.get('sha256', None)
        self.sourceIp = kwargs.get('sourceIp', None)
        self.source = kwargs.get('source', None)
        self.type = kwargs.get('type', None)
        self.url = kwargs.get('url', None)


class DVEvent(object):
    def __init__(self, **kwargs):
        self.uuid = kwargs.get('uuid', None)
        process = kwargs.get('process', None)
        self.process = Process(**process) if process else None
        agent = kwargs.get('agent', None)
        self.agent = Agent(**agent) if agent else None
        event = kwargs.get('event', None)
        self.event = Event(**event) if event else None
