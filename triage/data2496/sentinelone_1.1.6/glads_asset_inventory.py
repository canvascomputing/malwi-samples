from management import logger
from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import GLOBAL_ASSET_INVENTORY


class GladsAssetInventoryFilter(QueryFilter):
    QUERY_ARGS = {
        'agentId': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'limit': ['eq'],
        'skip': ['eq'],
    }

    def __init__(self):
        super(GladsAssetInventoryFilter, self).__init__()


class GlobalAssetsInventory(object):

    def __init__(self, client):
        self.client = client

    def get(self, query_filter=None, **filter_args):
        """
        Get global assets inventory
        Parameters:
        agentId=153154812615616132
        sortBy=appliedAt
        sortOrder=asc/desc
        limit=10
        skip=0
        """
        query_params = GladsAssetInventoryFilter.get_query_params(query_filter, filter_args)
        res = self.client.get(endpoint=GLOBAL_ASSET_INVENTORY, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get glads asset inventory, response_code: {}".format(res.json))
            raise_from_response(res)
        return res
