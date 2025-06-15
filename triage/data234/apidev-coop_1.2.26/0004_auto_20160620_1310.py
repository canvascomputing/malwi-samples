# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.urlresolvers import reverse


def set_homepage(apps, schema_editor):
    # Move from homepage_for_site to SiteSettings
    site_class = apps.get_model("sites", "Site")
    for site in site_class.objects.all():
        try:
            homepage_article = site.homepage_article.all()[0]
        except (models.ObjectDoesNotExist, IndexError, AttributeError):
            homepage_article = None

        if homepage_article:
            site_settings_class = apps.get_model("coop_cms", "SiteSettings")
            site_settings = site_settings_class.objects.get_or_create(site=site)[0]
            if not site_settings.homepage_url:
                homepage_url = reverse('coop_cms_view_article', args=[homepage_article.slug])
                site_settings.homepage_url = homepage_url
                site_settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0003_auto_20160204_1540'),
    ]

    operations = [
        migrations.RunPython(set_homepage),
    ]
