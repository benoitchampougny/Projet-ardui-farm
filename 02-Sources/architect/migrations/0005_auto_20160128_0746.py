# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0004_auto_20160128_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arduino',
            name='i2cPorts',
            field=models.ManyToManyField(default=None, to='architect.I2cPort', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='raspberry',
            name='i2cPorts',
            field=models.ManyToManyField(default=None, to='architect.I2cPort', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='raspberry',
            name='wifiPorts',
            field=models.ManyToManyField(default=None, to='architect.WifiPort', null=True, blank=True),
        ),
    ]
