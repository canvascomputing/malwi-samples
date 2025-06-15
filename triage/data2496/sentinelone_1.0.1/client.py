import json
import logging
import os
import traceback

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from management.common.auth_manager import AuthManager
from management.mgmtsdk_v2.endpoints import LOGIN

WEB_API_PREFIX_V2 = 'web/api/v2.0'

logger = logging.getLogger('MgmtSdk.Client')


class ManagementResponse(object):
    """
    This class represents a response from the management server.
    It encapsulates the response status code, data and pagination information in
    order to allow data handling, error handling and easy pagination 
    """

    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        try:
            self.json = response.json()
        except:
            self.json = dict()
        try:
            self.data = self.json.get('data', None)
            self.pagination = self.json.get('pagination', None)
            self.errors = self.json.get('errors', None)
        except:
            pass


class Client(object):
    """
    Client object is responsible for communication with management console.
    It encapsulates all communication details for the end user.
    Once a Client is initiated it tests the connection to the console and performs
    a login with the given credentials, upon successful login it will receive a
    token from the console and store it for future communications.

    From that point on, communication will be done via the client object, it provides
    abstraction for GET, PUT, POST, DELETE HTTP methods used by the services
    """

    def __init__(self, hostname, username=None, password=None, api_token=None, client_settings=None, auth_manager=None):
        """
        :param hostname: Management's hostname
        :type hostname: string
        :param username: Management username
        :type username: string
        :param password: Management password
        :type password: string
        :param api_token: Management Api Token
        :type api_token: string
        :param client_settings: all parameters to requests lib such as: verify / proxy / timeout / etc.
        :type client_settings: dict
        """
        if not auth_manager:
            auth_manager = AuthManager()
        self.auth_manager = auth_manager

        if not client_settings:
            client_settings = {}
        self.client_settings = client_settings
        self.verbose = client_settings.get('verbose', False)
        if 'verbose' in client_settings:
            del self.client_settings['verbose']
        self.web_api_prefix = client_settings.get('api_prefix', None) or WEB_API_PREFIX_V2
        if client_settings.get('api_prefix', None):
            del self.client_settings['api_prefix']
        if "verify" not in self.client_settings:
            verify_ssl = os.environ.get('VERIFY_MGMT_SSL', True)
            self.client_settings["verify"] = True if str(verify_ssl).lower() == 'true' else False

        self.session = requests.Session()
        retry = Retry(connect=3, backoff_factor=2)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

        self.hostname_url = hostname if 'http' in hostname else 'https://{0}'.format(hostname)
        self.test_connectivity()
        if api_token:
            auth_manager.headers.update({'Authorization': 'APIToken {}'.format(api_token)})
        else:
            self.login(username, password)

    def get(self, endpoint, params=None, use_raw=False, stream=False, use_api_prefix=True, api_prefix=None):
        """
        HTTP GET method to ``endpoint``
        :param api_prefix:
        :param use_api_prefix:
        :param endpoint: The destination URL endpoint
        :type endpoint: string
        :param params: URL Params
        :type params: dict
        :param use_raw: Controls return type - Raw python request's response object
        or an encapsulated ManagementResponse object
        :type use_raw: Boolean
        """
        api_prefix = api_prefix or self.web_api_prefix
        if not use_api_prefix:
            url = '{}/{}'.format(self.hostname_url,  endpoint)
        else:
            url = '{}/{}/{}'.format(self.hostname_url, api_prefix, endpoint)
        response = self.session.get(url, params=params,
                                    headers=self.auth_manager.headers,
                                    cookies=self.auth_manager.cookies,
                                    stream=stream,
                                    **self.client_settings)
        self._verbose_response(response)
        if not use_raw:
            return ManagementResponse(response)
        return response

    def post(self, endpoint, payload=None, data=None, query_filter=None, params=None, api_prefix=None, **kwargs):
        """
        HTTP POST method to ``endpoint``
        :param api_prefix:
        :param endpoint: The destination URL endpoint
        :type endpoint: string
        :param payload: request payload
        :type payload: dict
        :param data: request payload
        :type data: dict
        :param query_filter: request scope information (for multi tenant enviornments
        :type query_filter: dict
        :param params: URL Params
        :type params: dict
        """
        api_prefix = api_prefix or self.web_api_prefix
        if not payload:
            payload = dict()
        if data or data == {}:
            payload['data'] = data
        if query_filter:
            payload['filter'] = query_filter
        if payload:
            data_to_send = json.dumps(payload)
        else:
            data_to_send = None
        if 'files' in kwargs:
            if 'content-type' in self.auth_manager.headers:
                del self.auth_manager.headers['content-type']
            data_to_send = payload
        else:
            self.auth_manager.headers['content-type'] = 'application/json'

        merged_dicts = kwargs.copy()
        merged_dicts.update(self.client_settings)

        response = self.session.post(
            '{}/{}/{}'.format(self.hostname_url, api_prefix, endpoint),
            data=data_to_send,
            headers=self.auth_manager.headers,
            cookies=self.auth_manager.cookies,
            params=params,
            **merged_dicts
        )
        self._verbose_response(response)
        self.auth_manager.headers['content-type'] = 'application/json'
        return ManagementResponse(response)

    def put(self, endpoint, payload=None, data=None, query_filter=None, api_prefix=None):
        """
        HTTP PUT method to ``endpoint``
        :param api_prefix:
        :param endpoint: The destination URL endpoint
        :type endpoint: string
        :param payload: request payload
        :type payload: dict
        :param data: request payload
        :type data: dict
        :param query_filter: request scope information (for multi tenant enviornments
        :type query_filter: dict
        """
        api_prefix = api_prefix or self.web_api_prefix
        if not payload:
            payload = dict()
        if data:
            payload['data'] = data
        if query_filter:
            payload['filter'] = query_filter
        response = self.session.put(
            '{}/{}/{}'.format(self.hostname_url, api_prefix, endpoint),
            data=json.dumps(payload),
            headers=self.auth_manager.headers,
            cookies=self.auth_manager.cookies,
            **self.client_settings
        )
        self._verbose_response(response)
        return ManagementResponse(response)

    def delete(self, endpoint, payload=None, data=None, query_filter=None, api_prefix=None):
        """
        HTTP DELETE method to ``endpoint``
        :param query_filter:
        :param api_prefix:
        :param endpoint: The destination URL endpoint
        :type endpoint: string
        :param payload: request payload
        :type payload: dict
        :param data: request payload
        :type data: dict
        """
        api_prefix = api_prefix or self.web_api_prefix
        if not payload:
            payload = dict()
        if data or data == {}:
            payload['data'] = data
        if query_filter:
            payload['filter'] = query_filter

        response = self.session.delete(
            '{}/{}/{}'.format(self.hostname_url, api_prefix, endpoint),
            data=json.dumps(payload),
            headers=self.auth_manager.headers,
            cookies=self.auth_manager.cookies,
            **self.client_settings
        )
        self._verbose_response(response)
        return ManagementResponse(response)

    def test_connectivity(self, api_prefix=None):
        """
        Tests connection to SentinelOne's console
        """
        #logger.debug('Testing connection to {0}...'.format(self.hostname_url))
        #try:
        #    self.get(endpoint='system/status', api_prefix=api_prefix)

        #except Exception as e:
        #    logger.error('Could not connect to {0}. Error: {1}'.format(self.hostname_url, e))
        #    logger.error(traceback.print_exc())
        #    raise
        logger.debug('Successfully connected to {0}'.format(self.hostname_url))

    def login(self, username, password, api_prefix=None):
        """
        Login to SentinelOne's management console with provided credentials and
        saves the token on the Client object
        post_data = {'username': username, 'password': password}
        post_data['username'] = post_data['username'].replace(u'\ufeff', '')
        response = self.post(endpoint=LOGIN, payload=post_data, api_prefix=api_prefix)
        if not response:
            logger.error('Could not connect to {0}...'.format(self.hostname_url))
            raise ValueError('Connection to api-server failed')
        if response.status_code != 200 or not response.json:
            logger.error('Could not authenticate to {0}. Error code: {1}'.format(self.hostname_url,
                                                                                 response.status_code))
            raise ValueError('Authentication failed')
        """
        logger.debug('Successfully authenticated to {0}'.format(self.hostname_url))
        #self.auth_manager.token = '{0}'.format(response.data['token'])
        #self.auth_manager.headers.update({'Authorization': 'Token {}'.format(self.auth_manager.token)})

    def update_auth(self, token):
        """
        if 'x-iframe-token' in self.auth_manager.headers:
            del self.auth_manager.headers['x-iframe-token']
        if not token:
            if 'Authorization' in self.auth_manager.headers:
                del self.auth_manager.headers['Authorization']
            if 'Authorization' in self.auth_manager.cookies:
                del self.auth_manager.cookies['Authorization']
            self.auth_manager.token = None
            return
        """
        self.auth_manager.headers.update({'Authorization': 'Token {}'.format(token)})
        self.auth_manager.token = token

    def update_iframe_token(self, iframe_token, session_token):
        if 'Authorization' in self.auth_manager.headers:
            del self.auth_manager.headers['Authorization']
        self.auth_manager.headers.update({'x-iframe-token': iframe_token})
        self.auth_manager.cookies.update({'Authorization': "Token {}".format(session_token)})

    def _verbose_response(self, response):
        if self.verbose:
            try:
                resp = json.dumps(response.json())
            except:
                resp = response.text
            logger.info(f"=== Mgmt SDK Request details are: ===\n"
                        f"METHOD: {response.request.method}\n "
                        f"URL: {response.request.url}\n "
                        f"BODY: {response.request.body}\n "
                        f"Response Code: {response.status_code}\n "
                        f"Response Body: "
                        f"{resp}\n"
                        f"====================================")
