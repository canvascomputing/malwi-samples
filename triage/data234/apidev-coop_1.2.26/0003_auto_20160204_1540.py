# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0002_auto_20160108_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=datetime.datetime(2016, 2, 4, 15, 40, 3, 30106), verbose_name='created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=datetime.datetime(2016, 2, 4, 15, 40, 22, 708986), verbose_name='modified', auto_now=True),
            preserve_default=False,
        ),
    ]
