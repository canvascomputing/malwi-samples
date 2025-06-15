import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2_1.endpoints import *

from management.mgmtsdk_v2.exceptions import raise_from_response


logger = logging.getLogger('AgentActions')


class AgentActionsFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'activeThreats': ['eq', 'gt', 'gte', 'lt', 'lte', 'between'],
        'adQuery': ['eq'],
        'agentVersions': ['eq'],
        'computerName': ['eq', 'like'],
        'coreCount': ['gt', 'gte', 'lt', 'lte', 'between'],
        'createdAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'cpuCount': ['gt', 'gte', 'lt', 'lte', 'between'],
        'lastActiveDate': ['gt', 'gte', 'lt', 'lte', 'between'],
        'domains': ['eq'],
        'encryptedApplications': ['eq'],
        'externalId': ['eq'],
        'filterId': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'infected': ['eq'],
        'installerTypes': ['eq'],
        'isActive': ['eq'],
        'isDecommissioned': ['eq'],
        'isPendingUninstall': ['eq'],
        'isUninstalled': ['eq'],
        'isUpToDate': ['eq'],
        'localConfiguration': ['eq'],
        'mitigationMode': ['eq'],
        'mitigationModeSuspicious': ['eq'],
        'machineTypes': ['eq'],
        'networkStatuses': ['eq'],
        'osArch': ['eq'],
        'osTypes': ['eq'],
        'query': ['eq'],
        'registeredAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'scanStatus': ['eq'],
        'scanStatuses': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq'],
        'totalMemory': ['gt', 'gte', 'lt', 'lte', 'between'],
        'threatContentHash': ['eq'],
        'threatCreatedAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'threatHidden': ['eq'],
        'userActionsNeeded': ['eq'],
        'uuid': ['eq'],
        'uuids': ['eq'],

    }

    def __init__(self):
        super(AgentActionsFilter, self).__init__()


class AgentsDangerousActionFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'filterId': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'isUninstalled': ['eq'],
        'isDecommissioned': ['eq'],
        'query': ['eq'],
        'siteIds': ['eq'],
    }

    def __init__(self):
        super(AgentsDangerousActionFilter, self).__init__()


class AgentActions(object):

    def __init__(self, client):
        self.client = client

    def reset_local_config_to_policy(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=RESET_LOCAL_CONFIG, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to reset local config to policy, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def approve_uninstall(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=APPROVE_UNINSTALL, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to approve uninstall, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def reject_uninstall(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=REJECT_UNINSTALL, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to reject uninstall, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def restart(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentsDangerousActionFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=RESTART, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to restart, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def reload(self, module, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentsDangerousActionFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=RELOAD, data={"module": module}, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to reload, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def update_software(self, osType=None, fileName=None, absolute_path=None, package_id=None, isScheduled=None,
                        package_type=None, query_filter=None, allowDowngrade=None, **action_args):
        """
        Provide one of fileName/absolute_path params

        :param absolute_path:
        :param osType: type of OS
        :type  osType: string
        :param package_id: id of package
        :type package_id: string
        :param package_type: type of package
        :type package_type: string
        :param fileName:
        :type fileName: string
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param allowDowngrade: is allowed to downgrade
        :type allowDowngrade: bool
        :isScheduled: if immediate upgrade value should be false
        :type package_id: bool
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """

        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        post_data = {}
        if osType:
            post_data['osType'] = osType
        if fileName:
            post_data['fileName'] = fileName
        if absolute_path:
            post_data['path'] = absolute_path
        if package_id:
            post_data['packageId'] = package_id
        if package_type:
            post_data['packageType'] = package_type
        if isScheduled is not None:
            post_data['isScheduled'] = isScheduled
        if allowDowngrade is not None:
            post_data['allowDowngrade'] = allowDowngrade

        res = self.client.post(endpoint=UPDATE_SOFTWARE, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to update software, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def initiate_scan(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=INITIATE_SCAN, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to initiate scan, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def decommission(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentsDangerousActionFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=DECOMMISSION, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to decommission, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def move_agents_to_site(self, target_site_id, query_filter=None, **action_args):
        """
        :param target_site_id:
        :type target_site_id: string
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=MOVE_AGENTS_TO_SITE,
                               data={'targetSiteId': target_site_id}, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to move agents to site, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def fetch_logs(self, agent_logs=True, customer_facing_logs=True, platform_logs=False,
                   query_filter=None, **action_args):
        """
        :param agent_logs:
        :param platform_logs:
        :param customer_facing_logs:
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=FETCH_LOGS, query_filter=query_params,
                               data={'agentLogs': agent_logs, 'customerFacingLogs': customer_facing_logs,
                                     'platformLogs': platform_logs})
        if res.status_code != 200:
            logger.warning("Failed to fetch logs, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def abort_scan(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=ABORT_SCAN, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to abort scan, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def disconnect_from_network(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentsDangerousActionFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=DISCONNECT_FROM_NETWORK, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to disconnect from network, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def set_persistent_config_overrides(self, config, query_filter=None, **action_args):
        """
        :param config: config to override policy
        :type: config: dict
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=SET_PERSISTENT_CONFIG_OVERRIDES,
                               data={'config': config}, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set persistent config overrides, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def broadcast_message(self, message, query_filter=None, **action_args):
        """
        :param message: message to send to agents
        :type message: string
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=BROADCAST_MESSAGE, data={'message': message}, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to broadcast message, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def uninstall(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentsDangerousActionFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=UNINSTALL, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to uninstall, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def shutdown(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentsDangerousActionFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=SHUTDOWN, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to shutdown, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def connect_to_network(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=CONNECT_TO_NETWORK, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to connect to network, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def fetch_files(self, agent_id, files_list, password):
        """
        :param agent_id: id of agent to fetch files from
        :type agent_id: string
        :param files_list: list of files
        :type files_list: list
        :param password:
        :type password: strming
        :return: success status
        :rtype: ManagementResponse
        """
        post_data = {'files': files_list, 'password': password}
        res = self.client.post(endpoint=FETCH_FILES.format(agent_id), data=post_data)
        if res.status_code != 200:
            logger.warning("Failed to fetch files, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def move_to_console(self, token, query_filter=None, **action_args):
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=MOVE_TO_CONSOLE, query_filter=query_params, data={'token': token})
        if res.status_code not in [200, 201]:
            logger.warning("Failed to move to console, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data["affected"])
        return res

    def clear_remote_shell_session(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=CLEAR_REMOTE_SHELL, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to connect to network, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def start_remote_shell_session(self, historyPassword, twoFaCode, rows, columns, query_filter=None, **action_args):
        """
        :param historyPassword:
        :param twoFaCode:
        :param rows:
        :param columns:
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        data = {'historyPassword': historyPassword, 'twoFaCode':twoFaCode, 'columns': columns, 'rows': rows}
        res = self.client.post(endpoint=START_REMOTE_SHELL, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning("Failed start remote shell session, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def can_start_remote_shell_session(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=CAN_START_REMOTE_SHELL, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to check if can start remote shell session, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def terminate_remote_shell_session(self, channel_id, query_filter=None, **action_args):
        """
        :param channel_id:
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=TERMINATE_REMOTE_SHELL,
                               query_filter=query_params,
                               data={'channelId': channel_id})
        if res.status_code != 200:
            logger.warning("Failed to terminate remote shell session, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def fetch_installed_apps(self, query_filter=None, **action_args):
        """
        :param channel_id:
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=FETCH_INSTALLED_APPS, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed fetch installed apps, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def randomize_uuid(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=RANDOMIZE_UUID, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to randomize uuid, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def firewall_logging(self, report_mgmt, report_log, query_filter=None, **action_args):
        """
        :param report_mgmt:
        :param report_log:
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=FIREWALL_LOGGING, query_filter=query_params,
                               data={'reportMgmt': report_mgmt, 'reportLog': report_log})
        if res.status_code != 200:
            logger.warning("Failed to send firewall_logging, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def set_external_id(self, external_id, query_filter=None, **action_args):
        """
        :param external_id: New external_id for all matching agents
        :type external_id: str
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=SET_EXTERNAL_ID, query_filter=query_params,
                               data={'externalId': external_id})
        if res.status_code != 200:
            logger.warning("Failed to set external id, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def mark_as_up_to_date(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=MARK_AS_UP_TO_DATE, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to mark as up to date, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def fetch_applications(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentsDangerousActionFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=FETCH_APPLICATIONS, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to fetch applications, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def disable_agent(self, should_reboot, expiration=None, query_filter=None, **action_args):
        """
        :param should_reboot: Reboot the machine when disabling agent
        :type should_reboot: bool
        :param expiration: Activate agent after this timestamp (UTC)
        :type expiration: datetime
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        data = {'shouldReboot': should_reboot}
        if expiration:
            data['expiration'] = expiration.isoformat() + "Z"
        res = self.client.post(endpoint=DISABLE_AGENT, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning("Failed to fetch applications, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def enable_agent(self, should_reboot, query_filter=None, **action_args):
        """
        :param should_reboot: Reboot the machine when enabling agent
        :type should_reboot: bool
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        data = {'shouldReboot': should_reboot}
        res = self.client.post(endpoint=ENABLE_AGENT, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning("Failed to fetch applications, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def start_remote_profiling(self, timeout, query_filter=None, **action_args):
        """
        :param timeout: Disable remote profiling after that many seconds
        :type timeout: bool
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        data = {'timeout': timeout}
        res = self.client.post(endpoint=START_REMOTE_PROFILING, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning("Failed to fetch applications, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def stop_remote_profiling(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=STOP_REMOTE_PROFILING, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to fetch applications, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def disable_ranger(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=DISABLE_RANGER, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to disable ranger, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def enable_ranger(self, query_filter=None, **action_args):
        """
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=ENABLE_RANGER, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning("Failed to enable ranger, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def approve_stateless_upgrade(self, expiration, query_filter=None, **action_args):
        """
        :param expiration: expiration of approval
        :type expiration: str
        :param query_filter: Query filter object
        :type query_filter: AgentActionsFilter
        :param action_args: Key value with query filters
        :type action_args: **dict
        :return: number of affected agents
        :rtype: ManagementResponse
        """
        query_params = AgentActionsFilter.get_query_params(query_filter, action_args)
        res = self.client.post(endpoint=APPROVE_STATELESS_UPGRADE, query_filter=query_params,
                               data={'expiration': expiration})
        if res.status_code != 200:
            logger.warning("Failed to approve stateless upgrade, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res
