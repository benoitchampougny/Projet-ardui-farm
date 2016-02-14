# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0011_auto_20160208_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arduinomodel',
            name='analogIn',
        ),
        migrations.RemoveField(
            model_name='arduinomodel',
            name='ioPins',
        ),
        migrations.RemoveField(
            model_name='arduinomodel',
            name='pwmPins',
        ),
        migrations.AddField(
            model_name='arduinomodel',
            name='pinouts',
            field=models.ManyToManyField(to='architect.Pin'),
        ),
    ]
