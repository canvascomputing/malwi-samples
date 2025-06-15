# -*- coding: utf-8 -*-
""""test special pages"""

from unittest import skipIf

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.middleware.csrf import REASON_NO_REFERER, REASON_NO_CSRF_COOKIE
from django.test.client import RequestFactory
from django.test.utils import override_settings

from coop_cms.tests import BaseTestCase, BeautifulSoup
from coop_cms.settings import install_csrf_failure_view
from coop_cms.views.webutils import csrf_failure


@skipIf(getattr(settings, 'COOP_CMS_DO_NOT_INSTALL_CSRF_FAILURE_VIEW', False), "coop_cms csrf failure disabled")
class CsrfFailureTest(BaseTestCase):
    """Check custom page on CSRF failure"""
    
    def test_view_reason_cookie(self):
        """Check custom page with csrf cookie"""
        factory = RequestFactory()
        request = factory.get('/')
        request.user = AnonymousUser()
        
        response = csrf_failure(request, REASON_NO_CSRF_COOKIE)
        
        self.assertEqual(403, response.status_code)
        soup = BeautifulSoup(response.content)
        
        self.assertEqual(1, len(soup.select('.cookies-error')))
        self.assertEqual(0, len(soup.select('.referer-error')))
        self.assertEqual(0, len(soup.select('.unknown-error')))

    def test_view_reason_referer(self):
        """Check custom page with CSRF referer"""
        factory = RequestFactory()
        request = factory.get('/')
        request.user = AnonymousUser()
        
        response = csrf_failure(request, REASON_NO_REFERER)
        
        self.assertEqual(403, response.status_code)
        soup = BeautifulSoup(response.content)
        
        self.assertEqual(0, len(soup.select('.cookies-error')))
        self.assertEqual(1, len(soup.select('.referer-error')))
        self.assertEqual(0, len(soup.select('.unknown-error')))
    
    def test_view_reason_unknown(self):
        """Check custom page with unknown"""
        factory = RequestFactory()
        request = factory.get('/')
        request.user = AnonymousUser()
        
        response = csrf_failure(request, "?")
        
        self.assertEqual(403, response.status_code)
        soup = BeautifulSoup(response.content)
        
        self.assertEqual(0, len(soup.select('.cookies-error')))
        self.assertEqual(0, len(soup.select('.referer-error')))
        self.assertEqual(1, len(soup.select('.unknown-error')))


@override_settings(CSRF_FAILURE_VIEW='')
class InstallCsrfFailureTest(BaseTestCase):
    """Check custom page on CSRF failure"""

    @override_settings(COOP_CMS_DO_NOT_INSTALL_CSRF_FAILURE_VIEW=False)
    def test_install_crsf_failure(self):
        install_csrf_failure_view()
        self.assertEqual(getattr(settings, 'CSRF_FAILURE_VIEW', ''), 'coop_cms.views.webutils.csrf_failure')

    @override_settings(COOP_CMS_DO_NOT_INSTALL_CSRF_FAILURE_VIEW=True)
    def test_do_not_install_crsf_failure(self):
        install_csrf_failure_view()
        self.assertNotEqual(getattr(settings, 'CSRF_FAILURE_VIEW', ''), 'coop_cms.views.webutils.csrf_failure')