import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('ThreatExplore_2.1')


class ThreatExploreQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'childrenDepth': ['eq'],
        'countOnly': ['eq'],
        'cursor': ['eq'],
        'eventTypes': ['eq'],
        'eventId': ['eq'],
        'fetchAllChildren': ['eq'],
        'format': ['eq'],
        'limit': ['eq'],
        'selectedEventId': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'withParentsChildren': ['eq'],
        'withParents': ['eq'],
    }

    def __init__(self):
        super(ThreatExploreQueryFilter, self).__init__()


class ThreatExplore(object):
    """ThreatExplore service"""

    def __init__(self, client):
        self.client = client

    def get_events(self, threat_id, query_filter=None, **event_args):
        """
        Get all threat events
        :type threat_id
        :type query_filter: ThreatExploreQueryFilter
        :rtype: ManagementResponse
        """
        query_params = ThreatExploreQueryFilter.get_query_params(query_filter, event_args)
        res = self.client.get(endpoint=GET_EVENTS.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning(
                "Failed to get threat explore all threat events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def count_events_by_type(self, threat_id, query_filter=None, **event_args):
        """
        Get threat events count by type
        :type threat_id
        :type query_filter: ThreatExploreQueryFilter
        :rtype: ManagementResponse
        """
        query_params = ThreatExploreQueryFilter.get_query_params(query_filter, event_args)
        res = self.client.get(endpoint=COUNT_EVENTS_BY_TYPE.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning(
                "Failed to get threat explore count threat events by type, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_enriched_events(self, threat_id, query_filter=None, **event_args):
        """
        Get all threat events, enriched with extra attributes
        :type threat_id
        :type query_filter: ThreatExploreQueryFilter
        :rtype: ManagementResponse
        """
        query_params = ThreatExploreQueryFilter.get_query_params(query_filter, event_args)
        res = self.client.get(endpoint=GET_ENRICHED_EVENTS.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning(
                "Failed to get threat explore threat enriched events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_tree(self, threat_id, with_parents=False, query_filter=None, **event_args):
        """
        Get tree view for threat events
        :type threat_id
        :type with_parents
        :type query_filter: ThreatExploreQueryFilter
        :rtype: ManagementResponse
        """
        query_params = ThreatExploreQueryFilter.get_query_params(query_filter, event_args)
        query_params['withParents'] = with_parents
        res = self.client.get(endpoint=GET_TREE.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat explore threat tree, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def export_events(self, threat_id, query_filter=None, **event_args):
        """
        Export threat events in CSV format
        :type threat_id
        :type query_filter: ThreatExploreQueryFilter
        :rtype: ManagementResponse
        """
        query_params = ThreatExploreQueryFilter.get_query_params(query_filter, event_args)
        res = self.client.get(endpoint=EXPORT_EVENTS.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to export threat explore threat events, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
