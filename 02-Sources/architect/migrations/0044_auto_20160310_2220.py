# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0043_auto_20160310_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='actuator',
        ),
        migrations.RemoveField(
            model_name='element',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='element',
            field=models.ManyToManyField(to='architect.Element', blank=True),
        ),
    ]
