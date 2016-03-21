# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0049_auto_20160314_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatormodel',
            name='brand',
            field=models.CharField(default=datetime.datetime(2016, 3, 15, 18, 12, 2, 779673, tzinfo=utc), max_length=200, verbose_name=b'Brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='shortUnit',
            field=models.CharField(default='utc', max_length=200, verbose_name=b'Short Unit'),
            preserve_default=False,
        ),
    ]
