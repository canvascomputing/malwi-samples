# -*- coding: utf-8 -*-
""""""

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection

from coop_cms.models import Alias
from coop_cms.settings import is_localized


class Command(BaseCommand):
    """patch alias redirect"""
    help = u"patch alias redirect"
    use_argparse = False

    def handle(self, *args, **options):
        """command"""
        #look for emailing to be sent
        verbose = options.get('verbosity', 1)
        
        if not is_localized():
            print "the site is not localized this is not required"
        
        from modeltranslation.utils import build_localized_fieldname
        
        for alias in Alias.objects.all():
            cursor = connection.cursor()
            
            cursor.execute(
                '''SELECT path, redirect_url FROM coop_cms_alias where id={0}'''.format(alias.id))
            row = cursor.fetchone()
            print row
            (path, redirect_url) = row
            
            languages = [x for (x, y) in settings.LANGUAGES]
            
            lang_code = languages[0]
            path_field_name = build_localized_fieldname('path', lang_code)
            redirect_url_field_name = build_localized_fieldname('redirect_url', lang_code)
            if (not getattr(alias, path_field_name)) and (not getattr(alias, redirect_url_field_name)):
                print "update", alias.id, path, redirect_url
                setattr(alias, path_field_name, path)
                setattr(alias, redirect_url_field_name, redirect_url)
                alias.save()
