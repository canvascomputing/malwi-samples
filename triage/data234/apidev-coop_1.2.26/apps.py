# -*- coding: utf-8 -*-
"""
Basic app for article
"""

from django import VERSION

if VERSION > (1, 7, 0):
    from django.apps import AppConfig

    class BasicCmsAppConfig(AppConfig):
        name = 'coop_cms.apps.basic_cms'
        verbose_name = "coop CMS > Basic CMS"
