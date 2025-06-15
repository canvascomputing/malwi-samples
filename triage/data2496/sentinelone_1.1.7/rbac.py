import logging

from management.common.query_filter import HighScopeFilter
from management.mgmtsdk_v2.endpoints import RBAC_GET_USER_ROLE, RBAC_GET_ROLES, RBAC_GET_USER_PERMISSIONS
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2.services import Rbac as rbacV2

logger = logging.getLogger('Rbac')


class Rbac(rbacV2):

    def create_rbac_role(self, rbac_role, query_filter=None, **kwargs):
        query_params = HighScopeFilter.get_query_params(query_filter, kwargs)
        res = self.client.post(endpoint='rbac/role', data=rbac_role.to_json(), query_filter=query_params,
                               payload={'filter': {}})
        if res.status_code != 200:
            logging.warning("Failed to create rbac roles, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def update_rbac_role(self, role_id, **kwargs):
        res = self.client.put(endpoint=RBAC_GET_USER_ROLE.format(role_id), data=kwargs)
        if res.status_code != 200:
            logging.warning("Failed to update rbac role, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def delete_rbac_role(self, role_id, **kwargs):
        res = self.client.delete(endpoint=RBAC_GET_USER_ROLE.format(role_id), data=kwargs, payload={'data': {}})
        if res.status_code != 200:
            logging.warning("Failed to delete rbac role, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def get_rbac_role_template(self, **kwargs):
        res = self.client.get(endpoint='rbac/role', params=kwargs)
        if res.status_code != 200:
            logging.warning("Failed to Get rbac role template, response_code: {}".format(res.json))
            raise_from_response(res)
        return res