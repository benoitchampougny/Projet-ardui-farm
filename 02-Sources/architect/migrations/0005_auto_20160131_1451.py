# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0004_i2cport_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberry',
            name='wifiPorts',
            field=models.ManyToManyField(to='architect.WifiPort', blank=True),
        ),
    ]
