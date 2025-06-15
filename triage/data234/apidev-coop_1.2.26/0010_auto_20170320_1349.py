# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def set_alias_sites(apps, schema_editor):
    # Associate every alias with all sites
    site_class = apps.get_model("sites", "Site")
    alias_class = apps.get_model("coop_cms", "Alias")

    for alias in alias_class.objects.all():
        for site in site_class.objects.all():
            alias.sites.add(site)
        alias.save()


def reset_alias_sites(apps, schema_editor):
    # Clear the sites for all alias
    alias_class = apps.get_model("coop_cms", "Alias")

    for alias in alias_class.objects.all():
        alias.sites.clear()
        alias.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('coop_cms', '0009_auto_20170301_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='alias',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', verbose_name='sites', blank=True),
        ),
        migrations.RunPython(set_alias_sites, reset_alias_sites),
    ]
