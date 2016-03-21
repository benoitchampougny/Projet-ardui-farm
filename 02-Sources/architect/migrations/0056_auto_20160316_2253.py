# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0055_sensormodel_boolean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensormodel',
            name='element',
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='element',
            field=models.ForeignKey(default=None, blank=True, to='architect.Element', null=True),
        ),
    ]
