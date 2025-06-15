# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0008_alias_redirect_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='homepage_article',
            field=models.CharField(default='', max_length=256, blank=True, help_text='if set, the homepage will get the article with the given slug', verbose_name='homepage article', db_index=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='homepage_url',
            field=models.CharField(default='', max_length=256, blank=True, help_text='if set, the homepage will be redirected to the given URL', verbose_name='homepage URL', db_index=True),
        ),
    ]
