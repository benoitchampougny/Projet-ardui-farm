# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='i2cport',
            name='connection',
            field=models.ManyToManyField(related_name='connection_rel_+', to='architect.I2cPort'),
        ),
        migrations.AddField(
            model_name='wifiport',
            name='connection',
            field=models.ManyToManyField(related_name='connection_rel_+', to='architect.WifiPort'),
        ),
    ]
