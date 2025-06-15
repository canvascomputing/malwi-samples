# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def set_links_sites(apps, schema_editor):
    # Associate every links with all sites
    site_class = apps.get_model("sites", "Site")
    link_class = apps.get_model("coop_cms", "Link")

    for link in link_class.objects.all():
        for site in site_class.objects.all():
            link.sites.add(site)
        link.save()


def reset_links_sites(apps, schema_editor):
    # Clear the sites for all links
    link_class = apps.get_model("coop_cms", "Link")

    for link in link_class.objects.all():
        link.sites.clear()
        link.save()


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0011_auto_20170502_1124'),
    ]

    operations = [
        migrations.RunPython(set_links_sites, reset_links_sites)
    ]

