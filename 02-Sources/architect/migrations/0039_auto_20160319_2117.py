# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0038_auto_20160319_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalport',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='digitalport',
            name='pins',
        ),
        migrations.DeleteModel(
            name='DigitalPort',
        ),
    ]
