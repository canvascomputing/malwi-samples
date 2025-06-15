# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0006_image_copyright'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='newsletter_date',
            field=models.DateField(default=None, null=True, verbose_name='newsletter date', blank=True),
        ),
    ]
