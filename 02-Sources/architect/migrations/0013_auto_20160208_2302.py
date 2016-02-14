# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0012_auto_20160208_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arduinomodel',
            name='pinouts',
        ),
        migrations.AddField(
            model_name='pin',
            name='arduino',
            field=models.ForeignKey(default=1, to='architect.ArduinoModel'),
            preserve_default=False,
        ),
    ]
