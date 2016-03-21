# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0051_auto_20160315_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pingroup',
            name='goupfunctions',
        ),
        migrations.AddField(
            model_name='pingroup',
            name='goupFunctionModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.GroupFunctionModel', null=True),
        ),
    ]
