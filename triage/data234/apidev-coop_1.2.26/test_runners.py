# -*- coding: utf-8 -*-
"""customize execution of tests"""

from django.test.runner import DiscoverRunner

from coop_cms.settings import get_unit_test_media_root


class SafeMediaDiscoverRunner(DiscoverRunner):
    """change media root for unit tests"""

    def run_tests(self, *args, **kwargs):
        get_unit_test_media_root()
        super(SafeMediaDiscoverRunner, self).run_tests(*args, **kwargs)
