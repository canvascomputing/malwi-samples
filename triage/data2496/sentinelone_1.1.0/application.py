import logging

from management.mgmtsdk_v2.endpoints import GET_INSTALLED_APPS, GET_CVES, GET_CVES_ENRICHED, GET_FREE_TEXT_FILTERS, \
    GET_FILTERS_AUTO_COMPLETE, GET_FILTERS_COUNT, GET_RISK_LEVELS_COUNT, GROUPED_APP_INVENTORY, APP_INVENTORY_COUNTS
from management.mgmtsdk_v2.exceptions import raise_from_response

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.entities.installed_application import InstalledApplication, Cve, CveEnriched

logger = logging.getLogger('InstalledApplications')


class ApplicationsFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'agentComputerName': ['contains'],
        'agentMachineTypes': ['eq'],
        'agentOsVersion': ['contains'],
        'agentUuid': ['contains'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'groupIds': ['eq'],
        'filteredSiteIds': ['eq'],
        'filteredGroupIds': ['eq'],
        'installedAt': ['between'],
        'ids': ['eq'],
        'limit': ['eq'],
        'name': ['contains'],
        'publisher': ['contains'],
        'osTypes': ['eq'],
        'riskLevel': ['eq'],
        'riskLevels': ['eq'],
        'siteIds': ['eq'],
        'size': ['between'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'types': ['eq'],
        'type': ['eq'],
        'version': ['contains'],

    }

    def __init__(self):
        super(ApplicationsFilter, self).__init__()


class AppInventoryFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'countOnly': ['eq'],
        'createdAt': ['lt', 'gt'],
        'groupIds': ['eq'],
        'limit': ['eq'],
        'osTypes': ['eq'],
        'siteIds': ['eq'],
        'skipCount': ['eq'],
    }

    def __init__(self):
        super(AppInventoryFilter, self).__init__()


class AutoCompleteFilter(ApplicationsFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'agentComputerName': ['contains'],
        'agentMachineTypes': ['eq'],
        'agentOsVersion': ['contains'],
        'agentUuid': ['contains'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'filteredSiteIds': ['eq'],
        'filteredGroupIds': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'installedAt': ['between'],
        'key': ['eq'],
        'limit': ['eq'],
        'name': ['contains'],
        'osTypes': ['eq'],
        'publisher': ['contains'],
        'riskLevel': ['eq'],
        'riskLevels': ['eq'],
        'siteIds': ['eq'],
        'size': ['between'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'text': ['eq'],
        'type': ['eq'],
        'types': ['eq'],
        'version': ['contains'],
    }

    def __init__(self):
        super(AutoCompleteFilter, self).__init__()


class CvsFilter(QueryFilter):

    QUERY_ARGS = {
        'accountIds': ['eq'],
        'applicationIds': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'cveIds': ['eq'],
        'groupIds': ['eq'],
        'ids': ['eq'],
        'limit': ['eq'],
        'siteIds': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
    }

    def __init__(self):
        super(CvsFilter, self).__init__()


class Applications(object):
    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **app_args):
        query_params = ApplicationsFilter.get_query_params(query_filter, app_args)
        ret = list()
        res = self.client.get(endpoint=GET_INSTALLED_APPS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get installed apps, response_code: {}".format(res.status_code))
            raise_from_response(res)
        applications = res.data
        for application in applications:
            ret.append(InstalledApplication(**application))
        res.data = ret
        return res

    def get_cves(self, query_filter=None, **app_args):
        query_params = CvsFilter.get_query_params(query_filter, app_args)
        ret = list()
        res = self.client.get(endpoint=GET_CVES, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get cves, response_code: {}".format(res.status_code))
            raise_from_response(res)
        cves = res.data
        for cve in cves:
            ret.append(Cve(**cve))
        res.data = ret
        return res

    def get_cves_enriched(self, agent_application_id):
        res = self.client.get(endpoint=GET_CVES_ENRICHED.format(agent_application_id))
        if res.status_code != 200:
            logger.warning("Failed to get cves enriched, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = CveEnriched(**res.data)
        return res

    def get_free_text_filters(self):
        res = self.client.get(endpoint=GET_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning("Failed to get free text filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_filters_auto_complete(self, key, text, query_filter=None, **app_args):
        query_params = AutoCompleteFilter.get_query_params(query_filter, app_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=GET_FILTERS_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get auto complete filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def count_by_filters(self, query_filter=None, **app_args):
        query_params = ApplicationsFilter.get_query_params(query_filter, app_args)
        res = self.client.get(endpoint=GET_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get applications count by filters, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_count_by_risk_level(self, query_filter=None, **app_args):
        query_params = ApplicationsFilter.get_query_params(query_filter, app_args)
        res = self.client.get(endpoint=GET_RISK_LEVELS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get applications count by risk level, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def grouped_app_inventory(self, query_filter=None, **activity_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ActivitiesFilter
        :param activity_args: Key value with query filters
        :type activity_args: **dict
        :return: grouped application inventory
        :rtype: ManagementResponse
        """
        query_params = AppInventoryFilter.get_query_params(query_filter, activity_args)
        res = self.client.get(endpoint=GROUPED_APP_INVENTORY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get grouped app inventory, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def app_inventory_counts(self, query_filter=None, **activity_args):
        """
        :param query_filter: Query filter object
        :type query_filter: ActivitiesFilter
        :param activity_args: Key value with query filters
        :type activity_args: **dict
        :return: app inventory counts
        :rtype: ManagementResponse
        """
        query_params = AppInventoryFilter.get_query_params(query_filter, activity_args)
        res = self.client.get(endpoint=APP_INVENTORY_COUNTS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get grouped app inventory, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
