# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basic_cms', '0002_auto_20150924_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
