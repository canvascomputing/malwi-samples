# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import coop_cms.models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_cms', '0003_auto_20160129_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(db_index=True, max_length=100, unique=True, null=True, validators=[coop_cms.models.validate_slug]),
        ),
    ]
