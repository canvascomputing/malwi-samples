# -*- coding: utf-8 -*-

from coop_cms.utils import RequestManager, RequestMiddleware, RequestNotFound
from coop_cms.tests import BaseTestCase


class RequestManagerTest(BaseTestCase):
    """Test request manager"""
    
    def test_get_request(self):
        """retrieve request"""
        request1 = {'user': "joe"}
        RequestMiddleware().process_request(request1)
        request2 = RequestManager().get_request()
        self.assertEqual(request1, request2)
        
    def test_get_request_no_middleware(self):
        """if no request"""
        RequestManager().clean()
        self.assertRaises(RequestNotFound, RequestManager().get_request)
