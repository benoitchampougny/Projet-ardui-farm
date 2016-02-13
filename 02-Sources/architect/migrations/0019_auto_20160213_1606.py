# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0018_auto_20160213_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i2cport',
            name='connection',
            field=models.ManyToManyField(related_name='connection_rel_+', to='architect.I2cPort', blank=True),
        ),
        migrations.AlterField(
            model_name='wifiport',
            name='connection',
            field=models.ManyToManyField(related_name='connection_rel_+', to='architect.WifiPort', blank=True),
        ),
    ]
