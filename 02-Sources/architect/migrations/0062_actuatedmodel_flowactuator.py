# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0061_actuatedmodel_element'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatedmodel',
            name='flowActuator',
            field=models.BooleanField(default=False, verbose_name=b'Flow Actuator'),
        ),
    ]
