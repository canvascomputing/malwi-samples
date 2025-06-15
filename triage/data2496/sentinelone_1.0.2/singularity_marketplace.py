import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.endpoints import *

logger = logging.getLogger('SingularityMarketplace')


class SingularityMarketplaceQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'name': ['contains'],
        'category': ['contains'],
        'description': ['contains'],
        'id': ['eq'],
        'ids': ['eq'],
        'scopes': ['eq'],
        'applicationCatalogId': ['eq'],
        'tenant': ['eq'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'creator': ['eq'],
        'query': ['eq'],
        'limit': ['eq'],
        'cursor': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(SingularityMarketplaceQueryFilter, self).__init__()


class SingularityMarketplace(object):
    def __init__(self, client):
        self.client = client

    def get_applications_catalog(self, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_SINGULARITY_MARKETPLACE_APPS_CATALOG, params=query_params)
        if res.status_code != 200:
            logger.warning(f'Failed to get applications catalog, response_code: {res.status_code}')
            raise_from_response(res)
        return res.data

    def get_applications_catalog_config(self, app_catalog_id, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_SINGULARITY_MARKETPLACE_APPS_CATALOG_CONFIG.format(app_catalog_id),
                              params=query_params)
        if res.status_code != 200:
            logger.warning(f'Failed to get app catalog configuration '
                           f'(app_catalog_id={app_catalog_id}), response_code: {res.status_code}')
            raise_from_response(res)
        return res.data

    def get_applications(self, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_SINGULARITY_MARKETPLACE_APPLICATIONS, params=query_params)
        if res.status_code != 200:
            logger.warning(f'Failed to get installed apps, response_code: {res.status_code}')
            raise_from_response(res)
        return res.data

    def get_applications_config(self, app_id, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        res = self.client.get(endpoint=GET_SINGULARITY_MARKETPLACE_APPLICATIONS_CONFIG.format(app_id),
                              params=query_params)
        if res.status_code != 200:
            logger.warning(f'Failed to get installed app configuration (app_id={app_id}), '
                           f'response_code: {res.status_code}')
            raise_from_response(res)
        return res.data

    def install_application(self, app_catalog_id, configurations=None, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        query_params['applicationCatalogId'] = app_catalog_id

        if configurations is None:
            configurations = []
        data = {"configurations": configurations}

        res = self.client.post(endpoint=SINGULARITY_MARKETPLACE_INSTALL_APPLICATION, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning(f'Failed to get installed apps, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res.data

    def update_application_config(self, ids, configurations=None, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        query_params['ids'] = ids

        if configurations is None:
            configurations = []

        data = {"configurations": configurations}

        res = self.client.put(endpoint=SINGULARITY_MARKETPLACE_UPDATE_APPLICATION, query_filter=query_params, data=data)
        if res.status_code != 200:
            logger.warning(f'Failed to update application, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res.data

    def enable_application(self, app_id, query_filter=None, **kwargs):
        return self._enable_disable_app(app_id, 'enable', query_filter, **kwargs)

    def disable_application(self, app_id, query_filter=None, **kwargs):
        return self._enable_disable_app(app_id, 'disable', query_filter, **kwargs)

    def _enable_disable_app(self, app_id, mode, query_filter, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        query_params['applicationId'] = app_id

        res = self.client.post(endpoint=SINGULARITY_MARKETPLACE_ENABLE_DISABLE_APPLICATION.format(mode),
                               query_filter=query_params)
        if res.status_code != 200:
            logger.warning(f'Failed to {mode} application, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res.data

    def delete_application(self, ids, query_filter=None, **kwargs):
        query_params = SingularityMarketplaceQueryFilter.get_query_params(query_filter, kwargs)
        query_params['id'] = [ids]

        res = self.client.delete(endpoint=SINGULARITY_MARKETPLACE_DELETE_APPLICATION, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning(f'Failed to delete installed application, response_code: {res.status_code}')
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res.data
