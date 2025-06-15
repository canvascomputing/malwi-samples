import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2_1.entities.threat_action import Enrichments, AvailableActions, AvailableActionsCount, \
    ExecutedActions

logger = logging.getLogger('ThreatActionService')


class ThreatActionsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'entityType': ['eq'],
        'entityId': ['eq'],
        'interfaceGroupingKeys': ['contains'],
        'id': ['eq'],
        'ids': ['eq'],
        'scopes': ['eq'],
        'tenant': ['eq'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'query': ['eq'],
        'limit': ['eq'],
        'cursor': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(ThreatActionsQueryFilter, self).__init__()


class ThreatActions(object):
    """XDR Threat Action Service"""

    def __init__(self, client):
        self.client = client

    def get_enrichments(self, query_filter=None, **enrichment_args):
        """
        Get list of ``enrichments`` from the console by filters, default filter is empty

        :type query_filter: ThreatActionsQueryFilter
        :type enrichment_args: dict
        :rtype: MMSResponse
        """
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, enrichment_args)
        res = self.client.get(endpoint=GET_ENRICHMENTS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get threat enrichments, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = [Enrichments(**enrichment) for enrichment in res.data['enrichments']]
        return res

    def get_available_actions(self, query_filter=None, **kwargs):
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_AVAILABLE_ACTIONS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get available actions, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = [AvailableActions(**kwargs) for kwargs in res.data['availableActions']]
        return res

    def trigger_enrichments_calculation(self, entity_id, entity_type='threat', query_filter=None, **kwargs):
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, kwargs)
        query_params['entityId'] = entity_id
        query_params['entityType'] = entity_type

        res = self.client.post(endpoint=TRIGGER_ENRICHMENTS_CALCULATION, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning(f'Failed to get trigger enrichments calculation, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = res.data['success']
        return res.data

    def execute_actions(self, ids, query_filter=None, **kwargs):
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, kwargs)
        query_params['ids'] = ids

        res = self.client.post(endpoint=EXECUTE_ACTIONS, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning(f'Failed to get executed actions, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res.data

    def get_available_actions_count(self, query_filter=None, **kwargs):
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_AVAILABLE_ACTIONS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get available actions count, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = [AvailableActionsCount(**kwargs) for kwargs in res.data['availableActionsCount']]
        return res

    def recalculate_available_actions(self, entity_id, entity_type='threat', query_filter=None, **kwargs):
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, kwargs)
        query_params['entityId'] = entity_id
        query_params['entityType'] = entity_type

        res = self.client.post(endpoint=RECALCULATE_AVAILABLE_ACTIONS, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning(f'Failed to recalculate available actions, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = res.data['success']
        return res.data

    def get_executed_actions(self, query_filter=None, **kwargs):
        query_params = ThreatActionsQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_EXECUTED_ACTIONS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get executed actions, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = [ExecutedActions(**kwargs) for kwargs in res.data['executedActions']]
        return res
