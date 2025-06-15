# -*- coding: utf-8 -*-
"""send newsletter"""

import sys

from django import VERSION as DJANGO_VERSION
from django.conf import settings
from django.core.management import call_command


def get_and_configure_base_class():
    if DJANGO_VERSION >= (1, 7, 0):
        from django.core.management.commands import migrate
        return migrate.Command
    else:
        if 'south' in settings.INSTALLED_APPS:
            from south.management.commands.migrate import Command as SouthMigrateCommand
            south_migration_modules = getattr(settings, 'SOUTH_MIGRATION_MODULES', None)
            if not south_migration_modules:
                south_migration_modules = {}
            south_migration_modules['coop_cms'] = 'coop_cms.south_migrations'
            settings.SOUTH_MIGRATION_MODULES = south_migration_modules
            return SouthMigrateCommand
        else:
            raise ImportError("south is not set in INSTALLED_APPS")


class Command(get_and_configure_base_class()):
    """send newsletter"""
    help = u"migrate"
    #use_argparse = False

    def handle(self, *args, **options):
        """command"""

        super(Command, self).handle(*args, **options)
        if DJANGO_VERSION >= (1, 7, 0) and 'test' in sys.argv and 'modeltranslation' in settings.INSTALLED_APPS:
            call_command('sync_translation_fields', interactive=False)
