import logging
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2.endpoints import APIDOC_GET, APIDOC_GET_SWAGGER

logger = logging.getLogger('ApiDoc')


class ApiDoc(object):
    """ApiDoc Service"""
    def __init__(self, client):
        self.client = client

    def get(self):
        res = self.client.get(endpoint=APIDOC_GET, use_api_prefix=False)
        if res.status_code != 200:
            logger.warning("Failed to get apidoc, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_swagger(self):
        res = self.client.get(endpoint=APIDOC_GET_SWAGGER, use_api_prefix=False)
        if res.status_code != 200:
            logger.warning("Failed to get apidoc swagger, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res