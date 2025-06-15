from management.mgmtsdk_v2.mgmt import Management as Management_v2
from management.mgmtsdk_v2_1.endpoints import WEB_API_PREFIX_V2_1
from management.mgmtsdk_v2_1.services import Threats, ThreatsNotes, Settings, ThreatExplore, Agents, Dashboards,\
    AgentActions, NetworkQuarantine, Tags, Rogues, Rbac, SingularityMarketplace, RemoteScripts, Ranger, TagManager, \
    ThreatActions, Threat_Intel, AutoUpgradePolicy, AppManagement,api


class Management(Management_v2):
    """
    Management object provides all capabilities the SDK has to offer.
    The management object fields are the services which provides the APIs
    to communicate with the SentinelOne management console

    So for example, to perform threat related operations one should use the Management's
    object threat field, endpoint operations via Management's agents, etc
    """

    def __init__(self, hostname, username=None, password=None, api_token=None, client_settings=None, auth_manager=None):
        if not client_settings:
            client_settings = {}
        client_settings['api_prefix'] = WEB_API_PREFIX_V2_1
        super(Management, self).__init__(hostname, username, password, api_token, client_settings, auth_manager)
        self.agent_actions = AgentActions(self.client)
        self.agents = Agents(self.client)
        self.api = api.run()
        self.dashboards = Dashboards(self.client)
        self.network_quarantine = NetworkQuarantine(self.client)
        self.rbac = Rbac(self.client)
        self.rogues = Rogues(self.client)
        self.settings = Settings(self.client)
        self.tags = Tags(self.client)
        self.threat_explore = ThreatExplore(self.client)
        self.threats = Threats(self.client)
        self.threats_notes = ThreatsNotes(self.client)
        self.singularity_marketplace = SingularityMarketplace(self.client)
        self.remote_scripts = RemoteScripts(self.client)
        self.threat_intel = Threat_Intel(self.client)
        self.ranger = Ranger(self.client)
        self.tag_manager = TagManager(self.client)
        self.auto_upgrade_policy = AutoUpgradePolicy(self.client)
        self.threat_actions = ThreatActions(self.client)
        self.app_management = AppManagement(self.client)

    def __repr__(self):
        return '<management.mgmtsdk_v2.1.mgmt.Management: {}>'.format(self.hostname)
