# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0007_newsletter_newsletter_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='alias',
            name='redirect_code',
            field=models.IntegerField(default=301, choices=[(301, '301 - Permanent'), (302, '302 - Non permanent')]),
        ),
    ]
