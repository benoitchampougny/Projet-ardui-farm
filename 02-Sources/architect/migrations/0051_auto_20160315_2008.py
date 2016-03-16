# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0050_auto_20160315_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='pingroup',
            name='pin',
            field=models.ManyToManyField(to='architect.Pin', blank=True),
        ),
        migrations.RemoveField(
            model_name='pingroup',
            name='goupfunctions',
        ),
        migrations.AddField(
            model_name='pingroup',
            name='goupfunctions',
            field=models.ForeignKey(default=None, blank=True, to='architect.GroupFunction', null=True),
        ),
    ]
