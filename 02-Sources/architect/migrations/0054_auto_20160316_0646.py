# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0053_auto_20160315_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupfunction',
            name='groupFunctionModel',
        ),
        migrations.RemoveField(
            model_name='groupfunction',
            name='pin',
        ),
        migrations.DeleteModel(
            name='GroupFunction',
        ),
    ]
