import logging

from management.common.query_filter import QueryFilter, FullScopeFilter
from management.mgmtsdk_v2.endpoints import *

from management.mgmtsdk_v2.exceptions import raise_from_response, \
    InvalidFilterException

logger = logging.getLogger('System')

system_config_keys = ['maxCoreLicenses', 'globalTwoFaEnabled', 'advancedMode',
                      'unlimitedCore', 'rememberMeLength','unlimitedComplete',
                      'cloudIntelligenceOn', 'accessibleUrl', 'maxCompleteLicenses',
                      'allowDuplicateSite',
                      ]


def validate_system_config(system_config):
    for key in list(system_config):
        if key not in system_config_keys:
            raise InvalidFilterException('Unsupported key {} for system_config. '
                                         'Supported keys are {}'.format(key, ','.join(system_config_keys)))


class SystemQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'groupIds': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq']
    }

    def __init__(self):
        super(SystemQueryFilter, self).__init__()


class System(object):

    def __init__(self, client):
        self.client = client

    def enabled_features(self, query_filter=None, **system_args):
        """
        :param query_filter: Query filter object
        :type query_filter: SystemQueryFilter
        :param system_args: Key value with query filters
        :type system_args: **dict
        :return: enabled features
        :rtype: ManagementResponse
        """
        query_params = SystemQueryFilter.get_query_params(query_filter, system_args)
        res = self.client.get(endpoint=ENABLED_FEATURES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to enable features, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_config(self, query_filter=None, **system_args):
        """
        :param query_filter: Query filter object
        :type query_filter: SystemQueryFilter
        :param system_args: Key value with query filters
        :type system_args: **dict
        :return: Config answering the query
        :rtype: ManagementResponse
        """
        query_params = SystemQueryFilter.get_query_params(query_filter, system_args)
        res = self.client.get(endpoint=SYSTEM_CONFIG, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get system config, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def set_config(self, system_config, query_filter=None, **system_args):
        """
        :param system_config:
        :type system_config: dict
        :param query_filter: Query filter object
        :type query_filter: SystemQueryFilter
        :param system_args: Key value with query filters
        :type system_args: **dict
        :return: Config that was set
        """
        query_params = FullScopeFilter.get_query_params(query_filter, system_args)
        validate_system_config(system_config)
        res = self.client.put(endpoint=SYSTEM_CONFIG, data=system_config, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to set system config, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_status(self):
        """
        :param system status
        :return: health
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=SYSTEM_STATUS)
        if res.status_code != 200:
            logger.warning("Failed to get system status, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = res.data['health']
        return res

    def get_info(self):
        """
        :return: system info
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=SYSTEM_INFO)
        if res.status_code != 200:
            logger.warning("Failed to get system info, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_eula_config(self):
        """
        :param system status
        :return: res
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=SYSTEM_EULA_CONFIG)
        if res.status_code != 200:
            logger.warning("Failed to get system eula config, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

