# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0056_auto_20160316_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensormodel',
            name='boolean',
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='boolean',
            field=models.ForeignKey(default=None, blank=True, to='architect.Boolean', null=True),
        ),
    ]
