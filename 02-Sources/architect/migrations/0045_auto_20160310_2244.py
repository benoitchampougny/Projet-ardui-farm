# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0044_auto_20160310_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='i2cadress',
            name='actuator',
        ),
        migrations.RemoveField(
            model_name='i2cadress',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='i2cAdress',
            field=models.ManyToManyField(to='architect.I2cAdress', blank=True),
        ),
    ]
