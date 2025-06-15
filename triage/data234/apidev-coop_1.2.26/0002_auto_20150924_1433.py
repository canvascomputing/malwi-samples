# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='login_required',
            field=models.BooleanField(default=False, help_text='If true, only user with login/password will able to access the article', verbose_name='login required'),
        ),
    ]
