# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0037_auto_20160319_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wifiport',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='actuator',
            name='digitalPorts',
        ),
        migrations.RemoveField(
            model_name='arduino',
            name='digitalPorts',
        ),
        migrations.RemoveField(
            model_name='arduino',
            name='i2cPorts',
        ),
        migrations.RemoveField(
            model_name='raspberry',
            name='i2cPorts',
        ),
        migrations.RemoveField(
            model_name='raspberry',
            name='wifiPorts',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='digitalPorts',
        ),
        migrations.DeleteModel(
            name='WifiPort',
        ),
    ]
