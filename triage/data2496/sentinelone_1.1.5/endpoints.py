"""
This module contains all the endpoints the Management object uses to communicate
with the SentinelOne management
"""

WEB_API_PREFIX_V2_1 = 'web/api/v2.1'

# THREATS #
ADD_TO_BLACKLIST = 'threats/add-to-blacklist'
ADD_TO_EXCLUSIONS = 'threats/add-to-exclusions'
COUNT_BY_FILTERS = 'private/threats/filters-count'
DISABLE_ENGINES = 'threats/engines/disable'  # not in automation use
DV_ADD_TO_BLACKLIST = 'threats/dv-add-to-blacklist'
DV_MARK_AS_THREAT = 'threats/dv-mark-as-threat'
EXPORT_THREATS = 'threats/export'
FETCH_THREAT = 'threats/fetch-file'
GET_THREATS = 'threats'
MITIGATE_THREAT = 'threats/mitigate/{}'
CONTAINER_UNQ = 'threats/actions/container-network-connect'
CONTAINER_NQ = 'threats/actions/container-network-disconnect'
THREAT_GROUPS = 'private/threat-groups'
THREATS_AGENTS_DISCONNECT = 'private/threats/agents-disconnect'
THREATS_AGENTS_CONNECT = 'private/threats/agents-connect'
THREATS_FILTERS_AUTOCOMPLETE = 'private/threats/filters-autocomplete'
THREATS_SUMMARY = 'private/threats/summary'  # not in automation use
FREE_TEXT_FILTERS = 'private/threats/free-text-filters'
DOWNLOAD_THREAT_FROM_CLOUD = 'threats/{}/download-from-cloud'
AVAILABLE_ACTIONS = 'private/threats/available-actions'
THREAT_ANALYSIS = 'private/threats/{}/analysis'
THREAT_APPEARANCES = 'private/threats/{}/appearances'

GET_THREAT_NOTES = 'threats/{}/notes'
CREATE_THREAT_NOTE = 'threats/notes'
UPDATE_THREAT_NOTE = 'threats/{}/notes/{}'
DELETE_THREAT_NOTE = 'threats/{}/notes/{}'

THREAT_TIMELINE_CATEGORIES = 'private/threats/timeline-categories'
THREAT_TIMELINE = 'threats/{}/timeline'
EXPORT_THREAT_TIMELINE = 'export/threats/{}/timeline'

# SETTINGS #
USER_PREFERENCES = 'private/user-preferences'

# THREAT EXPLORE #
GET_TREE = 'private/threats/{}/explore/tree'
GET_ENRICHED_EVENTS = 'private/threats/{}/explore/all-events'
GET_EVENTS = 'threats/{}/explore/events'
EXPORT_EVENTS = 'export/threats/{}/explore/events'
COUNT_EVENTS_BY_TYPE = 'private/threats/{}/explore/count-by-type'

EXTERNAL_TICKET_ID = 'threats/external-ticket-id'
UPDATE_THREAT_ANALYST_VERDICT = 'threats/analyst-verdict'
UPDATE_THREAT_INCIDENT = 'threats/incident'
DOWNLOAD_MITIGATION_REPORT = 'threats/mitigation-report/{}'

GET_DASHBOARD = 'private/dashboard'

# AGENT ACTIONS #
AGENT_ACTIONS_COMMON_PREFIX = 'agents/actions'
AGENT_SUPPORT_ACTIONS_COMMON_PREFIX = 'private/agents/support-actions'
RESET_LOCAL_CONFIG = '{}/reset-local-config'.format(AGENT_ACTIONS_COMMON_PREFIX)
APPROVE_UNINSTALL = '{}/approve-uninstall'.format(AGENT_ACTIONS_COMMON_PREFIX)
REJECT_UNINSTALL = '{}/reject-uninstall'.format(AGENT_ACTIONS_COMMON_PREFIX)
RESTART = '{}/restart-machine'.format(AGENT_ACTIONS_COMMON_PREFIX)
RELOAD = '{}/reload'.format(AGENT_SUPPORT_ACTIONS_COMMON_PREFIX)
UPDATE_SOFTWARE = '{}/update-software'.format(AGENT_ACTIONS_COMMON_PREFIX)
INITIATE_SCAN = '{}/initiate-scan'.format(AGENT_ACTIONS_COMMON_PREFIX)
DECOMMISSION = '{}/decommission'.format(AGENT_ACTIONS_COMMON_PREFIX)
MOVE_AGENTS_TO_SITE = '{}/move-to-site'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_LOGS = '{}/fetch-logs'.format(AGENT_ACTIONS_COMMON_PREFIX)
ABORT_SCAN = '{}/abort-scan'.format(AGENT_ACTIONS_COMMON_PREFIX)
DISCONNECT_FROM_NETWORK = '{}/disconnect'.format(AGENT_ACTIONS_COMMON_PREFIX)
SET_PERSISTENT_CONFIG_OVERRIDES = '{}/set-config'.format(AGENT_ACTIONS_COMMON_PREFIX)
BROADCAST_MESSAGE = '{}/broadcast'.format(AGENT_ACTIONS_COMMON_PREFIX)
UNINSTALL = '{}/uninstall'.format(AGENT_ACTIONS_COMMON_PREFIX)
SHUTDOWN = '{}/shutdown'.format(AGENT_ACTIONS_COMMON_PREFIX)
CONNECT_TO_NETWORK = '{}/connect'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_FILES = 'agents/{}/actions/fetch-files'
MOVE_TO_CONSOLE = 'agents/actions/move-to-console'
START_REMOTE_SHELL = '{}/start-remote-shell'.format(AGENT_ACTIONS_COMMON_PREFIX)
CLEAR_REMOTE_SHELL = '{}/clear-remote-shell-session'.format(AGENT_ACTIONS_COMMON_PREFIX)
CAN_START_REMOTE_SHELL = '{}/can-start-remote-shell'.format(AGENT_ACTIONS_COMMON_PREFIX)
TERMINATE_REMOTE_SHELL = '{}/terminate-remote-shell'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_INSTALLED_APPS = '{}/fetch-installed-apps'.format(AGENT_ACTIONS_COMMON_PREFIX)
RANDOMIZE_UUID = '{}/randomize-uuid'.format(AGENT_ACTIONS_COMMON_PREFIX)
FIREWALL_LOGGING = '{}/firewall-logging'.format(AGENT_ACTIONS_COMMON_PREFIX)
SET_EXTERNAL_ID = '{}/set-external-id'.format(AGENT_ACTIONS_COMMON_PREFIX)
MARK_AS_UP_TO_DATE = '{}/mark-up-to-date'.format(AGENT_ACTIONS_COMMON_PREFIX)
FETCH_APPLICATIONS = '{}/fetch-installed-apps'.format(AGENT_ACTIONS_COMMON_PREFIX)
DISABLE_AGENT = '{}/disable-agent'.format(AGENT_ACTIONS_COMMON_PREFIX)
ENABLE_AGENT = '{}/enable-agent'.format(AGENT_ACTIONS_COMMON_PREFIX)
START_REMOTE_PROFILING = '{}/start-profiling'.format(AGENT_ACTIONS_COMMON_PREFIX)
STOP_REMOTE_PROFILING = '{}/stop-profiling'.format(AGENT_ACTIONS_COMMON_PREFIX)
DISABLE_RANGER = '{}/ranger-disable'.format(AGENT_ACTIONS_COMMON_PREFIX)
ENABLE_RANGER = '{}/ranger-enable'.format(AGENT_ACTIONS_COMMON_PREFIX)
APPROVE_STATELESS_UPGRADE = '{}/approve-stateless-upgrade'.format(AGENT_ACTIONS_COMMON_PREFIX)
TAG_MANAGER_ATTACH_ENDPOINT_TAGS = '{}/manage-tags'.format(AGENT_ACTIONS_COMMON_PREFIX)
TAG_MANAGER_DETACH_ENDPOINT_TAGS = '{}/manage-tags'.format(AGENT_ACTIONS_COMMON_PREFIX)


# AGENTS #
GET_AGENTS = 'agents'
COUNT_AGENTS = 'agents/count'
COUNT_AGENTS_BY_FILTERS = 'private/agents/filters-count'
AGENTS_FILTERS_AUTOCOMPLETE = 'private/agents/filters-autocomplete'
AGENTS_COUNT_SUMMARY = 'private/agents/summary'
GET_APPLICATIONS = 'agents/applications'
GET_PROCESSES = 'agents/processes'
GET_PASSPHRASES = 'agents/passphrases'
EXPORT_LOGS = 'agents/{}/uploads/{}'
TAG_MANAGER_GET_TAGS = 'agents/tags'

# TAGS #
TAGS = 'tags'
SPECIFIC_TAG = 'tags/{}'

# TAGS MANAGER #
TAG_MANAGER_CREATE_TAG = 'tag-manager'
TAG_MANAGER_EDIT_TAG = 'tag-manager/{}'
TAG_MANAGER_DELETE_TAG = 'tag-manager'

TAG_MANAGER_IMPORT_TAGS = 'tag-manager/import'
TAG_MANAGER_EXPORT_TAGS = 'tag-manager/export'

GET_USED_TAGS_FOR_ENDPOINT = 'tag-manager/endpoints/attached-tags'
# TAG_MANAGER_ATTACH_ENDPOINT_TAGS = 'tag-manager/endpoints/attach'
# TAG_MANAGER_DETACH_ENDPOINT_TAGS = 'tag-manager/endpoints/detach'
# TAG_MANAGER_ALTER_ENDPOINT_TAGS = 'tag-manager/endpoints/alter-tags'

# FIREWALL CONTROL #
NETWORK_QUARANTINE = 'firewall-control/network-quarantine'
NETWORK_QUARANTINE_REORDER = 'firewall-control/network-quarantine/reorder'
NETWORK_QUARANTINE_PRIVATE_FILTERS_COUNT = 'private/firewall-control/network-quarantine/filters-count'
NETWORK_QUARANTINE_UPDATE_RULE = 'firewall-control/{}'
NETWORK_QUARANTINE_SETTINGS = 'firewall-control/network-quarantine/configuration'
NETWORK_QUARANTINE_COPY_RULES = 'firewall-control/network-quarantine/copy-rules'
NETWORK_QUARANTINE_MOVE_RULES = 'firewall-control/network-quarantine/move-rules'
NETWORK_QUARANTINE_STATUS = 'firewall-control/network-quarantine/enable'
NETWORK_QUARANTINE_FREE_TEXT_FILTERS = 'private/firewall-control/network-quarantine/free-text-filters'
NETWORK_QUARANTINE_FILTER_AUTO_COMPLETE = 'private/firewall-control/network-quarantine/filters-autocomplete'
NETWORK_QUARANTINE_ADD_TAGS = 'firewall-control/network-quarantine/add-tags'
NETWORK_QUARANTINE_REMOVE_TAGS = 'firewall-control/network-quarantine/remove-tags'

ROGUES_DEVICE_INVENTORY_TABLE_VIEW = 'rogues/table-view'
ROGUES_FILTERS_COUNT = 'private/rogues/filters-count'
ROGUES_RANGER_FILTERS_COUNT = 'private/rogues/ranger/filters-count'
ROGUES_EXPORT_DEVICE_INVENTORY = 'rogues/report/csv'
ROGUES_FREE_TEXT_FILTERS = 'private/rogues/free-text-filters'
ROGUES_GET_SNAPSHOT_STATUS = 'private/rogues/snapshot-status'
ROGUES_GET_SETTINGS = 'rogues/settings'
ROGUES_UPDATE_SETTINGS = 'rogues/settings'
ROGUES_STATUS = 'private/rogues/status'

# STAR Alerts #
STAR_ALERTS = 'cloud-detection/alerts'
STAR_ANALYST_VERDICT = f'{STAR_ALERTS}/analyst-verdict'
STAR_INCIDENT = f'{STAR_ALERTS}/incident'

# SINGULARITY_MARKETPLACE #
GET_SINGULARITY_MARKETPLACE_APPS_CATALOG = "singularity-marketplace/applications-catalog"
GET_SINGULARITY_MARKETPLACE_APPS_CATALOG_CONFIG = "singularity-marketplace/applications-catalog/{}/config"
GET_SINGULARITY_MARKETPLACE_APPLICATIONS = "singularity-marketplace/applications"
GET_SINGULARITY_MARKETPLACE_APPLICATIONS_CONFIG = "singularity-marketplace/applications/{}/config"
SINGULARITY_MARKETPLACE_INSTALL_APPLICATION = "singularity-marketplace/applications"
SINGULARITY_MARKETPLACE_UPDATE_APPLICATION = "singularity-marketplace/applications"
SINGULARITY_MARKETPLACE_DELETE_APPLICATION = "singularity-marketplace/applications"
SINGULARITY_MARKETPLACE_ENABLE_DISABLE_APPLICATION = "singularity-marketplace/applications/{}"
NEXUS_BE_ADD_APPLICATION_CATALOG = "applications_catalog"
NEXUS_BE_UPDATE_APPLICATION_CATALOG = "applications_catalog/{}"
NEXUS_BE_DELETE_APPLICATION_CATALOG = "applications_catalog/{}"

# Remote Scripts Orchestration
REMOTE_SCRIPTS_GET_SCRIPTS = "remote-scripts"
REMOTE_SCRIPTS_ADD_SCRIPT = "remote-scripts"
REMOTE_SCRIPTS_EDIT_SCRIPT = "remote-scripts/{}"
REMOTE_SCRIPTS_DELETE_SCRIPT = "remote-scripts"
REMOTE_SCRIPTS_EXECUTE_SCRIPT = "remote-scripts/execute"
REMOTE_SCRIPTS_STATUS = "remote-scripts/status"
REMOTE_SCRIPTS_FETCH_FILES = "remote-scripts/fetch-files"

# RANGER #
RANGER_DEVICE_REVIEW = 'ranger/device-review'
RANGER_DEVICE_REVIEW_SINGLE = 'ranger/device-review/{}'
RANGER_DEVICE_REVIEW_REASONS = 'private/ranger/review-reasons'
RANGER_DEVICE_INVENTORY_TABLE_VIEW = 'ranger/table-view'
RANGER_FILTERS_COUNT = 'private/ranger/filters-count'
RANGER_EXPORT_DEVICE_INVENTORY = 'ranger/report/csv'
RANGER_FREE_TEXT_FILTERS = 'private/ranger/free-text-filters'
RANGER_FILTERS_AUTO_COMPLETE = 'private/ranger/filters-autocomplete'
RANGER_GET_ROW_JSON = 'ranger/{}/json'
RANGER_RAW_DATA_EXPORT = 'ranger/{}/json/export'
RANGER_GET_SNAPSHOT_STATUS = 'private/ranger/snapshot-status'
RANGER_GET_LATEST_SNAPSHOT = 'private/ranger/latest-snapshot'
RANGER_GET_GATEWAYS = 'ranger/gateways'
RANGER_UPDATE_GATEWAY = 'ranger/gateways/{}'
RANGER_UPDATE_GATEWAYS = 'ranger/gateways/update'
RANGER_NETWORK_DASHBOARD = 'private/ranger/gateways/dashboard'
RANGER_GET_SETTINGS = 'ranger/settings'
RANGER_UPDATE_SETTINGS = 'ranger/settings'
RANGER_SUBNET_SCAN_DATA = 'private/ranger/scan-data'
GATEWAY_FILTERS_COUNT = 'private/ranger/gateways/filters-count'
GATEWAY_FREE_TEXT_FILTERS = 'private/ranger/gateways/free-text-filters'
GATEWAY_FILTERS_AUTO_COMPLETE = 'private/ranger/gateways/filters-autocomplete'
RANGER_CRED_GROUP = 'ranger/cred-groups'
RANGER_CRED_GROUP_DETAILS = 'ranger/cred-groups/details'
RANGER_GET_AUTO_DEPLOY_DEPLOYERS = 'private/ranger/auto-deploy/get-deployers'
RANGER_AUTO_DEPLOY_START = 'private/ranger/auto-deploy/start'
RANGER_INIT_AUTO_DEPLOY_DEPLOYERS = 'ranger/auto-deploy/deploy'
DELETE_CRED_GROUP = 'ranger/cred-groups/'
DELETE_CRED_GROUP_DETAILS = 'ranger/cred-groups/details/'
RANGER_SELF_ENABLEMENT = 'ranger/enablement'
RANGER_SELF_ENABLEMENT_DEFAULTS = 'ranger/enablement/defaults'
RANGER_SELF_ENABLEMENT_MANAGEMENT = 'ranger/enable-self-management'
RANGER_LABEL_DEVICES = 'ranger/label-devices'
RANGER_LABEL_DEVICES_REVERT = 'ranger/revert-label-devices'
RANGER_LABEL_DEVICES_INFO = 'private/ranger/labelling-info'
RANGER_TAGS = 'ranger/tags'


# APPLICATION MANAGEMENT
APP_SCAN = 'application-management/scan'
APP_SCAN_STATUS = 'private/application-management/scan'
RISKS_GET = 'application-management/risks'
RISKS_EXPANDED = 'private/application-management/risks/expanded'
RISKS_FILTERS_COUNT = 'private/application-management/risks/filters-count'
RISKS_FREE_TEXT_FILTERS = 'private/application-management/risks/free-text-filters'
RISKS_AUTO_COMPLETE = 'private/application-management/risks/filters-autocomplete'
RISKS_EXPORT = 'application-management/risks/export/csv'

INVENTORY_GET = 'application-management/inventory'
INVENTORY_FILTERS_COUNT = 'private/application-management/inventory/filters-count'
INVENTORY_FREE_TEXT_FILTERS = 'private/application-management/inventory/free-text-filters'
INVENTORY_AUTO_COMPLETE = 'private/application-management/inventory/filters-autocomplete'
INVENTORY_EXPORT = 'application-management/inventory/export/csv'
INVENTORY_VERSIONS_COUNT = 'private/application-management/inventory/versions-count'

INVENTORY_ENDPOINTS = 'private/application-management/inventory/endpoints'
INVENTORY_ENDPOINTS_FILTERS_COUNT = 'private/application-management/inventory/endpoints/filters-count'
INVENTORY_ENDPOINTS_FREE_TEXT_FILTERS = 'private/application-management/inventory/endpoints/free-text-filters'
INVENTORY_ENDPOINTS_AUTO_COMPLETE = 'private/application-management/inventory/endpoints/filters-autocomplete'
INVENTORY_ENDPOINTS_EXPORT = 'application-management/inventory/endpoints/export/csv'

# THREAT INTELLIGENCE
THREAT_INTELLIGENCE = 'threat-intelligence/iocs'

# GLOBAL ASSET INVENTORY #
GLOBAL_ASSET_INVENTORY = 'content-updates-inventory'

# XDR THREAT ACTIONS
GET_ENRICHMENTS = 'private/threat-actions/enrichments'
GET_AVAILABLE_ACTIONS = 'private/threat-actions/available-actions'
TRIGGER_ENRICHMENTS_CALCULATION = 'private/threat-actions/recalculate-enrichments'
EXECUTE_ACTIONS = 'private/threat-actions/execute-actions'
GET_AVAILABLE_ACTIONS_COUNT = 'private/threat-actions/available-actions-count'
RECALCULATE_AVAILABLE_ACTIONS = 'private/threat-actions/recalculate-available-actions'
GET_EXECUTED_ACTIONS = 'private/threat-actions/executed-actions'

#UPGRADE POLICY
GET_UPGRADE_POLICIES = 'upgrade-policy/policies'
CREATE_UPGRADE_POLICIES = 'upgrade-policy/policy'
PARENT_UPGRADE_POLICIES = 'upgrade-policy/parent-policies'
REORDER_UPGRADE_POLICIES = 'upgrade-policy/reorder'
ACTION_UPGRADE_POLICY = 'upgrade-policy/policy/{}'
INHERITED_UPGRADE_POLICY = 'upgrade-policy/set-inheriting'
AGENT_VERSION_UPGRADE_POLICY = 'upgrade-policy/available-packages'
