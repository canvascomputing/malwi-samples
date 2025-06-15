import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.endpoints import GET_THREAT_FORENSIC_DETAILS, \
    GET_THREAT_CONNECTIONS, \
    GET_THREAT_FORENSICS, EXPORT_THREAT, GET_THREAT_SEEN_ON_NETWORK, \
    GET_APPLICATION_FORENSIC_DETAILS, \
    GET_APPLICATION_CONNECTIONS, EXPORT_APPLICATION, GET_APPLICATION_FORENSICS
from management.mgmtsdk_v2.entities.forensic import ThreatForensicDetails, \
    ThreatForensics, ThreatSeenOnNetwork, \
    ApplicationForensicDetails, ApplicationForensics

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('Forensics')


class ForensicsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'country_code': ['eq'],
        'groupId': ['in'],
        'siteId': ['in']

    }

    def __init__(self):
        super(ForensicsQueryFilter, self).__init__()


class Forensics(object):

    def __init__(self, client):
        self.client = client

    def get_threat_as_seen_on_network(self, threat_id, query_filter=None, **forensics_args):
        """
       :param threat_id: Id of threat to query
       :type threat_id: string
       :param query_filter: Query filter object
       :type query_filter: UpdateQueryFilter
       :param forensics_args: Key value with query filters
       :type forensics_args: **dict
       :return: ThreatSeenOnNetwork objects answering the query
       :rtype: ManagementResponse
       """
        query_params = ForensicsQueryFilter.get_query_params(query_filter, forensics_args)

        res = self.client.get(endpoint=GET_THREAT_SEEN_ON_NETWORK.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [ThreatSeenOnNetwork(**th) for th in res.data]
        return res

    #   TODO - implement using raw (when fixed on backend)
    def export_threat(self, threat_id):
        res = self.client.get(endpoint=EXPORT_THREAT.format(threat_id, 'raw'), use_raw=True)
        if res.status_code != 200:
            logger.warning("Failed to export threat, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_threat_forensics(self, threat_id):
        """
        :param threat_id: Id of threat to query
        :type threat_id: string
        :return: Forensics answering the query
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_THREAT_FORENSICS.format(threat_id))
        if res.status_code != 200:
            logger.warning("Failed to get threat forensics, response_code: {}".format(res.status_code))
            raise_from_response(res)

        if res.data["result"] is not None:
            res.data = ThreatForensics(**res.data["result"])
            return res

    def get_threat_forensic_details(self, threat_id):
        """
        :param threat_id: Id of threat to query
        :type threat_id: string
        :return: Forensics Details answering the query
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_THREAT_FORENSIC_DETAILS.format(threat_id))
        if res.status_code != 200:
            logger.warning("Failed to get threat forensic details, response_code: {}".format(res.status_code))
            raise_from_response(res)
        if res.data["result"] is not None:
            res.data = ThreatForensicDetails(**res.data["result"])
            return res

    def get_threat_connections(self, threat_id, query_filter=None, **forensics_args):
        """
        :param threat_id: Id of threat to query
        :type threat_id: string
        :param query_filter: Query filter object
        :type query_filter: UpdateQueryFilter
        :param forensics_args: Key value with query filters
        :type forensics_args: **dict
        :return: Threat connections
        :rtype: ManagementResponse
        """
        query_params = ForensicsQueryFilter.get_query_params(query_filter, forensics_args)

        res = self.client.get(endpoint=GET_THREAT_CONNECTIONS.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat connections, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def get_application_forensics(self, application_id, query_filter=None, **forensics_args):
        """
        :param application_id: Id of application to query
        :type application_id: string
        :return: Forensics answering the query
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_APPLICATION_FORENSICS.format(application_id))
        if res.status_code != 200:
            logger.warning("Failed to get application forensics, response_code: {}".format(res.status_code))
            raise_from_response(res)

        if res.data["result"] is not None:
            res.data = ApplicationForensics(**res.data["result"])
            return res

    def get_application_forensic_details(self, application_id, query_filter=None, **forensics_args):
        """
        :param application_id: Id of application to query
        :type application_id: string
        :return: Forensics Details answering the query
        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=GET_APPLICATION_FORENSIC_DETAILS.format(application_id))
        if res.status_code != 200:
            logger.warning("Failed to get application forensic details, response_code: {}".format(res.status_code))
            raise_from_response(res)
        if res.data["result"] is not None:
            res.data =  ApplicationForensicDetails(**res.data["result"])
            return res

    def get_application_connections(self, application_id, query_filter=None, **forensics_args):
        """
        :param application_id: Id of threat to query
        :type application_id: string
        :param query_filter: Query filter object
        :type query_filter: UpdateQueryFilter
        :param forensics_args: Key value with query filters
        :type forensics_args: **dict
        :return: Application connections
        :rtype: ManagementResponse
        """
        query_params = ForensicsQueryFilter.get_query_params(query_filter, forensics_args)

        res = self.client.get(endpoint=GET_APPLICATION_CONNECTIONS.format(application_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get application connections, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res

    def export_application(self, application_id):
        res = self.client.get(endpoint=EXPORT_APPLICATION.format(application_id, 'raw'), use_raw=True)
        if res.status_code != 200:
            logger.warning("Failed to export application, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
