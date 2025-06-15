import logging

from management.mgmtsdk_v2.endpoints import *
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Hash')


class Hashes(object):

    def __init__(self, client):
        self.client = client

    def classification(self, hash_id):
        """
        :param hash_id:
        :type hash_id: string
        :return: hash classification
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=HASH_CLASSIFICATION.format(hash_id))
        if res.status_code != 200:
            logger.warning("Failed to get hash classification by id, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def reputation(self, hash_id):
        """
        :param hash_id:
        :type hash_id: string
        :return: rank of hash
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=HASH_REPUTATION.format(hash_id))
        if res.status_code != 200:
            logger.warning("Failed to get hash reputation by id, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
