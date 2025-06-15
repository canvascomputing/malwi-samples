# -*- coding: utf-8 -*-
""""""

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, resolve, NoReverseMatch
from django.contrib.auth.views import redirect_to_login

from coop_cms.utils import get_login_url


class PermissionsMiddleware(object):
    """Handle permission"""

    def process_exception(self, request, exception):
        """manage exception"""

        if isinstance(exception, PermissionDenied) and (not request.user.is_authenticated()):
            try:
                login_url = get_login_url()
            except NoReverseMatch:
                login_url = None
            return redirect_to_login(request.path, login_url)
