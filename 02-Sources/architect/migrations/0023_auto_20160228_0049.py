# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0022_auto_20160225_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='LocationPorts',
            field=models.ManyToManyField(to='architect.LocationPort', blank=True),
        ),
        migrations.AddField(
            model_name='actuator',
            name='digitalPorts',
            field=models.ManyToManyField(to='architect.DigitalPort', blank=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='actuator',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='LocationPorts',
            field=models.ManyToManyField(to='architect.LocationPort', blank=True),
        ),
    ]
