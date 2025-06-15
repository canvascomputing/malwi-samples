import unittest

import mock

from dpp_client.clients import http


class BaseHTTPDPPClientTestCase(unittest.TestCase):

    def test_invalid_event_type(self):
        self.assertRaises(ValueError, http.DPPClient, 'url', None)
        self.assertRaises(ValueError, http.DPPClient, 'url', '')

    @mock.patch('dpp_client.clients.http.DPPClient._get_session')
    def test_init_session(self, get_session_mock):
        http.DPPClient(endpoint='http://example.com', event_type='client')

        self.assertEqual(get_session_mock.call_count, 1)
        self.assertEqual(get_session_mock.call_args_list[0], ())

    @mock.patch('requests.sessions.HTTPAdapter')
    @mock.patch('requests.Session.mount')
    @mock.patch('requests.Session')
    def test_init_session_adapter_default(self, session_mock, mount_mock,
                                          http_adapter_mock):
        http.DPPClient(endpoint='http://example.com', event_type='client')

        self.assertEqual(http_adapter_mock.call_count, 1)
        http_adapter_mock.assert_called_once_with()

    @mock.patch('requests.sessions.HTTPAdapter')
    @mock.patch('requests.Session.mount')
    @mock.patch('requests.Session')
    def test_init_session_adapter_all(self, session_mock, mount_mock,
                                      http_adapter_mock):
        adapter_kwargs = {'pool_connections': 13,
                          'pool_maxsize': 7,
                          'max_retries': 2,
                          'pool_block': True}

        http.DPPClient(endpoint='http://example.com', event_type='client',
                       adapter_kwargs=adapter_kwargs)

        self.assertEqual(http_adapter_mock.call_count, 1)
        http_adapter_mock.assert_called_once_with(**adapter_kwargs)

    @mock.patch('requests.sessions.HTTPAdapter')
    @mock.patch('requests.Session.mount')
    @mock.patch('requests.Session')
    def test_init_session_adapter_partial(self, session_mock, mount_mock,
                                          http_adapter_mock):
        adapter_kwargs = {'pool_connections': 3,
                          'max_retries': 1}

        http.DPPClient(endpoint='http://example.com', event_type='client',
                       adapter_kwargs=adapter_kwargs)

        self.assertEqual(http_adapter_mock.call_count, 1)
        http_adapter_mock.assert_called_once_with(**adapter_kwargs)
