# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0003_auto_20160131_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='i2cport',
            name='direction',
            field=models.CharField(default=b'DW', max_length=2, choices=[(b'UP', b'Upward'), (b'DW', b'Downward')]),
        ),
    ]
