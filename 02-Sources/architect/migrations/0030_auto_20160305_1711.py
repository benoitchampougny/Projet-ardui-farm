# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0029_auto_20160305_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='measure',
        ),
        migrations.AddField(
            model_name='unit',
            name='measure',
            field=models.ManyToManyField(default=None, to='architect.Measure', null=True, blank=True),
        ),
    ]
