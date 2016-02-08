# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0009_auto_20160206_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='arduino',
            name='digitalPorts',
            field=models.ManyToManyField(to='architect.DigitalPort', blank=True),
        ),
        migrations.AddField(
            model_name='digitalport',
            name='pwm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='digitalPorts',
            field=models.ManyToManyField(to='architect.DigitalPort', blank=True),
        ),
    ]
