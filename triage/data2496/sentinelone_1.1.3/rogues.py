import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import ROGUES_DEVICE_INVENTORY_TABLE_VIEW, ROGUES_FILTERS_COUNT, \
    ROGUES_EXPORT_DEVICE_INVENTORY, ROGUES_FREE_TEXT_FILTERS, ROGUES_GET_SNAPSHOT_STATUS, ROGUES_GET_SETTINGS, \
    ROGUES_UPDATE_SETTINGS, ROGUES_RANGER_FILTERS_COUNT

logger = logging.getLogger('Rogues')


class RoguesFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'tenant': ['eq'],
        'osType': ['eq', 'in'],
        'osName': ['eq'],
        'osVersion': ['eq', 'contains'],
        'localIp': ['eq', 'contains'],
        'externalIp': ['eq', 'contains'],
        'ids': ['eq'],
        'deviceType': ['eq', 'in'],
        'macAddress': ['eq', 'contains'],
        'gatewayMacAddress': ['eq', 'contains'],
        'firstSeen':  ['gt', 'gte', 'lt', 'lte', 'between'],
        'lastSeen':  ['gt', 'gte', 'lt', 'lte', 'between'],
        'manufacturer': ['eq', 'contains'],
        'hostnames': ['eq', 'contains'],
        'query': ['eq'],
        'limit': ['eq'],
        'skip': ['eq'],
        'cursor': ['eq'],
        'countOnly': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(RoguesFilter, self).__init__()


class Rogues(object):
    """Rogues service"""

    def __init__(self, client):
        self.client = client

    def get_device_inventory_table_view(self, query_filter=None, **rogues_args):
        query_params = RoguesFilter.get_query_params(query_filter, rogues_args)
        res = self.client.get(endpoint=ROGUES_DEVICE_INVENTORY_TABLE_VIEW, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get inventory table view, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_rogues_filters_count(self, query_filter=None, **rogues_args):
        query_params = RoguesFilter.get_query_params(query_filter, rogues_args)
        res = self.client.get(endpoint=ROGUES_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get rogues filters-count, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_rogues_ranger_filters_count(self, query_filter=None, **rogues_args):
        query_params = RoguesFilter.get_query_params(query_filter, rogues_args)
        res = self.client.get(endpoint=ROGUES_RANGER_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get rogues ranger filters-count, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def export_device_inventory(self, query_filter=None, **rogues_args):
        query_params = RoguesFilter.get_query_params(query_filter, rogues_args)
        res = self.client.get(endpoint=ROGUES_EXPORT_DEVICE_INVENTORY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to export rogues data to csv, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_rogues_free_text_filters(self):
        res = self.client.get(endpoint=ROGUES_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get rogues free text filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_snapshot_status(self, query_filter=None, **rogues_args):
        query_params = RoguesFilter.get_query_params(query_filter, rogues_args)
        res = self.client.get(endpoint=ROGUES_GET_SNAPSHOT_STATUS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get snapshot status, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_rogues_settings(self, query_filter=None, **rogues_args):
        query_params = RoguesFilter.get_query_params(query_filter, rogues_args)
        res = self.client.get(endpoint=ROGUES_GET_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get rogues settings, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def update_rogues_settings(self, account_ids, **kwargs):
        res = self.client.put(endpoint=ROGUES_UPDATE_SETTINGS, query_filter={'accountIds': account_ids}, data=kwargs)
        if res.status_code != 200:
            logger.warning("Failed to update rogues settings, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
