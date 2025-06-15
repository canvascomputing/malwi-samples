import json
import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2_1.entities.upgrade_policy import Package, ReOrder, UpgradePolicy

logger = logging.getLogger('upgrade_policy')


class AutoUpgradePolicyFilter(QueryFilter):
    QUERY_ARGS = {
        'osType': ['eq'],
        'scopeId': ['eq'],
        'scopeLevel': ['eq'],
        'limit': ['eq'],
        'skip': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(AutoUpgradePolicyFilter, self).__init__()


class AutoUpgradePolicy(object):
    """auto upgrade policy"""

    def __init__(self, client):
        self.client = client

    def get_upgrade_policies(self, query_filter=None, **args):
        """
            get all policies of a scope
        """
        query_params = AutoUpgradePolicyFilter.get_query_params(query_filter, args)
        res = self.client.get(endpoint=GET_UPGRADE_POLICIES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get all upgrade policies, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_parent_upgrade_policies(self, query_filter=None, **args):
        """
            get all parent policies of a scope
        """
        query_params = AutoUpgradePolicyFilter.get_query_params(query_filter, args)
        res = self.client.get(endpoint=PARENT_UPGRADE_POLICIES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get all parent upgrade policies, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def create_upgrade_policy(self, name: str, scope_id: int, scope_level: str, os_type: str, package: Package=None,
                              description='description', is_active=False, all_endpoints=True, tags=None,
                              is_scheduled=False):
        """
            Create new auto upgrade policy
        """
        upgrade_policy = UpgradePolicy(name=name, description=description, isActive=is_active, scopeLevel=scope_level,
                                       osType=os_type, package=package, allEndpoints=all_endpoints, scopeId=scope_id,
                                       tags=tags, isScheduled=is_scheduled)

        payload = json.loads(json.dumps(upgrade_policy, default=lambda o: o.__dict__))

        res = self.client.post(endpoint=CREATE_UPGRADE_POLICIES, payload=payload)
        if res.status_code != 200:
            logger.warning("Failed to create upgrade policy, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def edit_upgrade_policy(self, upgrade_policy_id: str, name: str, scope_id: str, scope_level: str, os_type: str,
                            package: Package,
                            description='description', is_active=False, all_endpoints=True, tags=None,
                            is_scheduled=False):
        """
            edit auto upgrade policy
        """
        upgrade_policy = UpgradePolicy(name=name, description=description,
                                       is_active=is_active, scopeLevel=scope_level, scopeId=scope_id, osType=os_type,
                                       package=package, allEndpoints=all_endpoints, tags=tags, isScheduled=is_scheduled)

        payload = json.loads(json.dumps(upgrade_policy, default=lambda o: o.__dict__))

        res = self.client.put(endpoint=ACTION_UPGRADE_POLICY.format(upgrade_policy_id), payload=payload)
        if res.status_code != 200:
            logger.warning("Failed to create upgrade policy, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def inherited_upgrade_policy(self, scope_id: str, scope_level: str, is_inherited=True,
                                 query_filter=None, **args):
        """
            inherited auto upgrade policy
        """
        data = {
            'isInheriting': is_inherited
        }
        query_params = AutoUpgradePolicyFilter.get_query_params(query_filter, args)
        data['scopeId'] = scope_id
        data['scopeLevel'] = scope_level
        res = self.client.put(endpoint=INHERITED_UPGRADE_POLICY, payload=data)
        if res.status_code != 200:
            logger.warning("Failed to inherited upgrade policy, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def reorder_upgrade_policies(self, reorders):
        """
            reorder auto upgrade policies
        """
        reorders_json = []
        for item in reorders:
            reorders_json.append(json.loads(item.to_json()))

        data = {
            'policies': reorders_json
        }

        res = self.client.put(endpoint=REORDER_UPGRADE_POLICIES, payload=data)
        if res.status_code != 200:
            logger.warning("Failed to reorder upgrade policies, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def action_upgrade_policy(self, upgrade_policy_id: str, action: str):
        """
            delete | activate | deactivate auto upgrade policy
        """
        data = {
            'action': action
        }

        res = self.client.post(endpoint=ACTION_UPGRADE_POLICY.format(upgrade_policy_id), payload=data)
        if res.status_code != 200:
            logger.warning(f"Failed to {action} upgrade policy, response_code: {res.json}")
            raise_from_response(res)
        return res

    def deactivate_all_upgrade_policies(self, scope_id: str, scope_level: str, os_type: str, query_filter=None, **args):
        """
            deactivate all policies in scope
        """
        query_params = AutoUpgradePolicyFilter.get_query_params(query_filter, args)
        query_params['scopeId'] = scope_id
        query_params['scopeLevel'] = scope_level
        query_params['osType'] = os_type
        res = self.client.post(endpoint=GET_UPGRADE_POLICIES, data={}, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to deactivate all policies on all upgrade policies, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_agent_versions_upgrade_policy(self, query_filter=None, **args):
        """
            get all agent versions
        """
        query_params = AutoUpgradePolicyFilter.get_query_params(query_filter, args)
        res = self.client.get(endpoint=AGENT_VERSION_UPGRADE_POLICY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get all parent upgrade policies, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
