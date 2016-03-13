# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0042_auto_20160309_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='actuator',
        ),
        migrations.RemoveField(
            model_name='measure',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='measure',
            field=models.ManyToManyField(to='architect.Measure', blank=True),
        ),
    ]
