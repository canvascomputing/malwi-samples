# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop_cms', '0004_auto_20160620_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='pagination_size',
            field=models.IntegerField(default=0, help_text='The number of articles to display in a category page. If 0, use default', verbose_name='pagination size'),
        ),
    ]
