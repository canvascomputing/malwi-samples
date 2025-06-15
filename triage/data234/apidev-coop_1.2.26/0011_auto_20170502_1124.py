# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('coop_cms', '0010_auto_20170320_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', blank=True),
        ),
    ]
