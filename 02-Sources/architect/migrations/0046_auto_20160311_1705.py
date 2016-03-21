# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0045_auto_20160310_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boolean',
            name='actuator',
        ),
        migrations.RemoveField(
            model_name='boolean',
            name='sensor',
        ),
        migrations.RemoveField(
            model_name='boolean',
            name='element',
        ),
        migrations.AddField(
            model_name='boolean',
            name='element',
            field=models.ManyToManyField(to='architect.Element', blank=True),
        ),
    ]
