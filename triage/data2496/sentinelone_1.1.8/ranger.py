from management.mgmtsdk_v2_1.endpoints import *
import logging
from management.common.query_filter import QueryFilter, BaseScopeFilter
from management.mgmtsdk_v2.entities.ranger import Gateway
from management.mgmtsdk_v2.exceptions import raise_from_response


logger = logging.getLogger('Ranger')


class RangerFilter(QueryFilter):
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
        'snapshotIds': ['eq'],
        'deviceType': ['eq', 'in'],
        'macAddress': ['eq', 'contains'],
        'gatewayMacAddress': ['eq', 'contains'],
        'firstSeen': ['gt', 'gte', 'lt', 'lte', 'between'],
        'lastSeen': ['gt', 'gte', 'lt', 'lte', 'between'],
        'agentIds': ['eq'],
        'managedState': ['eq'],
        'managedStates': ['eq'],
        'manufacturer': ['eq', 'contains'],
        'networkName': ['eq', 'contains'],
        'discoveryMethods': ['eq'],
        'hostnames': ['eq', 'contains'],
        'subnetAddress': ['contains'],
        'tcpPorts': ['contains'],
        'udpPorts': ['contains'],
        'query': ['eq'],
        'limit': ['eq'],
        'skip': ['eq'],
        'cursor': ['eq'],
        'countOnly': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'period': ['eq'],
    }

    def __init__(self):
        super(RangerFilter, self).__init__()


class RangerGatewayFilter(QueryFilter):
    QUERY_ARGS = {
        'externalIp': ['eq', 'contains'],
        'limit': ['eq'],
        'skip': ['eq'],
        'cursor': ['eq'],
        'countOnly': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
        'macAddress': ['eq', 'contains'],
        'ip': ['eq', 'contains'],
        'ids': ['eq'],
        'allowScan': ['eq'],
        'agentPercentage': ['gt', 'gte', 'lt', 'lte', 'between'],
        'numberOfAgents': ['gt', 'gte', 'lt', 'lte', 'between'],
        'numberOfRangers': ['gt', 'gte', 'lt', 'lte', 'between'],
        'totalAgents': ['gt', 'gte', 'lt', 'lte', 'between'],
        'createdAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'updatedAt': ['gt', 'gte', 'lt', 'lte', 'between'],
        'manufacturer': ['eq', 'contains'],
        'allowedScanners': ['contains'],
        'query': ['eq'],
        'tcpPorts': ['contains'],
        'udpPorts': ['contains'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'snmpScan': ['eq'],
        'mdnsScan': ['eq'],
        'rdnsScan': ['eq'],
        'smbScan': ['eq'],
        'icmpScan': ['eq'],
        'new': ['eq'],
        'archived': ['eq'],
        'scanOnlyLocalSubnets': ['eq'],
    }

    def __init__(self):
        super(RangerGatewayFilter, self).__init__()


class Ranger(object):
    """Ranger service"""
    def __init__(self, client):
        self.client = client

    def update_ranger_cred_group(self, group_name, group_passphrase, scope_id, domain=None, is_linux=False):
        if is_linux:
            data = {'groupName': group_name,
                    'groupPassphrase': group_passphrase,
                    'scopeId': scope_id, 'targetOs': 'osx_linux'}
        else:
            data = {'domain': domain, 'groupName': group_name,
                    'groupPassphrase': group_passphrase,
                    'scopeId': scope_id, 'targetOs': 'windows'}
        res = self.client.post(endpoint=RANGER_CRED_GROUP, data=data)
        if res.status_code != 200:
            logging.info(f"Failed to update ranger cred group, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_ranger_cred_group_details(self, account_id, site_id=None, **params):
        if site_id:
            params['siteIds'] = site_id
        else:
            params['accountIds'] = account_id
        res = self.client.get(endpoint=RANGER_CRED_GROUP_DETAILS, params=params)
        if res.status_code != 200:
            logging.info(f"Failed to get ranger cred group, response_code: {res.json}")
            raise_from_response(res)
        return res

    def set_ranger_cred_group_details(self, **kwargs):
        res = self.client.post(endpoint=RANGER_CRED_GROUP_DETAILS, data=kwargs)
        if res.status_code != 200:
            logging.info(f"Failed to get ranger cred group, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_auto_deploy_deployers(self, **ranger_args):
        res = self.client.get(endpoint=RANGER_GET_AUTO_DEPLOY_DEPLOYERS, params=ranger_args)
        if res.status_code != 200:
            logger.warning(f"Failed to get auto deploy deployers, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_auto_deploy_availability(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_AUTO_DEPLOY_START, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get auto deploy device availability, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def init_auto_deploy_deployers(self, **init_args):
        res = self.client.post(endpoint=RANGER_INIT_AUTO_DEPLOY_DEPLOYERS, data=init_args)
        if res.status_code != 200:
            logger.warning(f"Failed to init auto deploy deployer, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def delete_cred_group(self, group_id):
        res = self.client.delete(endpoint=f'{DELETE_CRED_GROUP}{group_id}')
        if res.status_code != 200:
            logger.warning(f"Failed to delete cred group, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def delete_cred_group_details(self, group_details_id):
        res = self.client.delete(endpoint=f'{DELETE_CRED_GROUP_DETAILS}{group_details_id}')
        if res.status_code != 200:
            logger.warning(f"Failed to delete cred group details, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def update_ranger_settings(self, account_ids=None, site_ids=None, **kwargs):
        if site_ids:
            query_filter = {'siteIds': site_ids}
        else:
            query_filter = {'accountIds': account_ids}
        res = self.client.put(endpoint=RANGER_UPDATE_SETTINGS, query_filter=query_filter, data=kwargs)
        if res.status_code != 200:
            logger.warning(f"Failed to update ranger settings, response_code: {res.json}")
            raise_from_response(res)
        return res

    def get_ranger_network_dashboard(self, query_filter=None, **ranger_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_NETWORK_DASHBOARD, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger network dashboard, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_subnet_scan_data(self, account_id, **params):
        params['accountIds'] = [account_id]
        res = self.client.get(endpoint=RANGER_SUBNET_SCAN_DATA, params=params)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger subnet scan data, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    # site_id
    def get_device_inventory_table_view(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_DEVICE_INVENTORY_TABLE_VIEW, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get inventory table view, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_ranger_filters_count(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger filters-count, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_gateway_filters_count(self, query_filter=None, **ranger_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=GATEWAY_FILTERS_COUNT, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get gateway filters-count, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def export_device_inventory(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_EXPORT_DEVICE_INVENTORY, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to export ranger data to csv, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_ranger_free_text_filters(self):
        res = self.client.get(endpoint=RANGER_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger free text filters, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_gateway_free_text_filters(self):
        res = self.client.get(endpoint=GATEWAY_FREE_TEXT_FILTERS)
        if res.status_code != 200:
            logger.warning(f"Failed to get gateway free text filters, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def ranger_filters_auto_complete(self, key, text, query_filter=None, **agent_args):
        query_params = RangerFilter.get_query_params(query_filter, agent_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=RANGER_FILTERS_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger autocomplete filters, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def gateway_filters_auto_complete(self, key, text, query_filter=None, **agent_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, agent_args)
        query_params['key'] = key
        query_params['text'] = text
        res = self.client.get(endpoint=GATEWAY_FILTERS_AUTO_COMPLETE, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get gateway autocomplete filters, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_raw_json(self, inventory_id):
        res = self.client.get(endpoint=RANGER_GET_ROW_JSON.format(inventory_id))
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger raw data, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def export_raw_data(self, inventory_id):
        res = self.client.get(endpoint=RANGER_RAW_DATA_EXPORT.format(inventory_id))
        if res.status_code != 200:
            logger.warning(f"Failed to export ranger raw data, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_snapshot_status(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_GET_SNAPSHOT_STATUS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get snapshot status, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_latest_snapshot(self):
        res = self.client.get(endpoint=RANGER_GET_LATEST_SNAPSHOT)
        if res.status_code != 200:
            logger.warning(f"Failed to get latest snapshot, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    # site_id
    def get_gateways(self, gateway_filter=None, **gateway_args):
        query_params = RangerGatewayFilter.get_query_params(gateway_filter, gateway_args)
        ret = list()
        res = self.client.get(endpoint=RANGER_GET_GATEWAYS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get gateways, response_code: {res.status_code}")
            raise_from_response(res)
        gateways = res.data
        for gateway in gateways:
            ret.append(Gateway(**gateway))
        res.data = ret
        return res

    # site_id
    def update_gateway(self, account_id, gateway_id, site_id=None, **kwargs):
        if site_id:
            scope = {'siteIds': site_id}
        else:
            scope = {'accountIds': account_id}
        gateway = self.get_gateways(**scope, ids=gateway_id).data[0]
        for key, val in kwargs.items():
            gateway.__setattr__(key, val)
        res = self.client.put(endpoint=RANGER_UPDATE_GATEWAY.format(gateway_id), data=gateway.to_json())
        if res.status_code != 200:
            logger.warning("Failed to update gateway, response_code: {}".format(res.json))
            raise_from_response(res)
        res.data = Gateway(**res.data)
        return res

    # site_id
    def update_gateways(self, allowscan, archived, query_filter=None, **ranger_args):
        query_params = RangerGatewayFilter.get_query_params(query_filter, ranger_args)
        res = self.client.post(endpoint=RANGER_UPDATE_GATEWAYS, data={'allowScan': allowscan, 'archived': archived},
                               payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning(f"Failed to update gateways, response_code: {res.json}")
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    # site_id
    def get_ranger_settings(self, query_filter=None, **ranger_args):
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_GET_SETTINGS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger settings, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_cred_group(self, **kwargs):
        res = self.client.get(endpoint=RANGER_CRED_GROUP, params=kwargs)
        if res.status_code != 200:
            logging.info(f"Failed to update ranger cred group, response_code: {res.json}")
            raise_from_response(res)
        return res

    def update_cred_group_details(self, cred_id, **kwargs):
        res = self.client.put(endpoint=f'{RANGER_CRED_GROUP_DETAILS}/{cred_id}', data=kwargs)
        if res.status_code != 200:
            logger.warning(f"Failed to update cred group details, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def toggle_enablement(self, toggle_state: bool, query_filter=None, **ranger_args):
        """ Sets Enable & disable state of a MSSP management feature """
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.post(endpoint=RANGER_SELF_ENABLEMENT_MANAGEMENT,
                               data={'enable': toggle_state},
                               payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning(f"Failed to update ranger enablement, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def set_enablement_defaults(self, ranger_pro=None, rogues=None, query_filter=None, **ranger_args):
        """ Sets defaults for newly created sites """
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        data = {}
        if ranger_pro is not None:
            data.update({'rangerProEnabled': ranger_pro})
        if rogues is not None:
            data.update({'roguesEnabled': rogues})
        res = self.client.post(endpoint=RANGER_SELF_ENABLEMENT_DEFAULTS, data=data, payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning(f"Failed to update ranger enablement defaults, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_enablement_status(self, account_id: str):
        """ Gets the enablement status of the sites under the given account """
        res = self.client.get(endpoint=RANGER_SELF_ENABLEMENT, params={'accountIds': account_id})
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger enablement, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def update_enablement(self, ranger_pro=None, rogues=None, query_filter=None, **ranger_args):
        """ Sets a scopeId with the Ranger & Rogues state """
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        data = {}
        if ranger_pro is not None:
            data.update({'rangerProEnabled': ranger_pro})
        if rogues is not None:
            data.update({'roguesEnabled': rogues})
        res = self.client.post(endpoint=RANGER_SELF_ENABLEMENT, data=data, payload={'filter': query_params})
        if res.status_code != 200:
            logger.warning(f"Failed to update ranger enablement, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def label_devices(self, device_function, os_type, os_version='Unknown', query_filter=None, **ranger_args):
        """ Change the labels of more than one device """
        query_filter = RangerFilter.get_query_params(query_filter, ranger_args)
        data = {'deviceFunction': device_function, 'osType': os_type, 'osVersion': os_version}
        res = self.client.post(endpoint=RANGER_LABEL_DEVICES, data=data, payload={'filter': query_filter})
        if res.status_code != 200:
            logger.warning(f"Failed to label ranger devices, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_labelling_info(self, scope_filter=None, **scope_args):
        """ Get labelling info for the scope """
        query_params = BaseScopeFilter.get_query_params(scope_filter, scope_args)
        res = self.client.get(endpoint=RANGER_LABEL_DEVICES_INFO, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get ranger device labels, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def revert_label_devices(self, query_filter=None, **ranger_args):
        """ Revert the labels of more than one device """
        query_filter = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.post(endpoint=RANGER_LABEL_DEVICES_REVERT, payload={'filter': query_filter})
        if res.status_code != 200:
            logger.warning(f"Failed to revert ranger device labels, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def tag_devices(self, tag_id=None, tags=None, query_filter=None, **ranger_args):
        """ Tags the filtered devices with the given tag_id / tags """
        if not (tag_id or tags):
            raise ValueError('Must enter either tag_id or list of tags')
        data = tags or [{"id": tag_id}]
        query_filter = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.post(endpoint=RANGER_TAGS, data=data, payload={'filter': query_filter})
        if res.status_code != 200:
            logger.warning(f"Failed to tag devices, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def review_devices(self, device_review, reason='', reason_details='', query_filter=None, **ranger_args):
        """ Add a review to the filtered devices """
        query_filter = RangerFilter.get_query_params(query_filter, ranger_args)
        data = {"deviceReview": device_review, "reason": reason, 'reasonDetails': reason_details}
        res = self.client.post(endpoint=RANGER_DEVICE_REVIEW, data=data, payload={'filter': query_filter})
        if res.status_code != 200:
            logger.warning(f"Failed to review devices, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = res.data['affected']
        return res

    def review_single_device(self, device_id, device_review, reason='', reason_details='',
                             query_filter=None, **ranger_args):
        """ Add a review to a single device"""
        query_filter = RangerFilter.get_query_params(query_filter, ranger_args)
        data = {"deviceReview": device_review, "reason": reason, 'reasonDetails': reason_details}
        res = self.client.put(endpoint=RANGER_DEVICE_REVIEW_SINGLE.format(device_id),
                              query_filter=query_filter, data=data)
        if res.status_code != 200:
            logger.warning(f"Failed to to review device {device_id}, response_code: {res.status_code}")
            raise_from_response(res)
        return res

    def get_device_review_reasons(self, query_filter=None, **ranger_args):
        """ Gets existing device review reasons """
        query_params = RangerFilter.get_query_params(query_filter, ranger_args)
        res = self.client.get(endpoint=RANGER_DEVICE_REVIEW_REASONS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get existing device review reasons, response_code: {res.status_code}")
            raise_from_response(res)
        return res
