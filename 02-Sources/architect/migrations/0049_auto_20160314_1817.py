# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0048_auto_20160313_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='measure',
        ),
        migrations.AddField(
            model_name='measure',
            name='unit',
            field=models.ManyToManyField(to='architect.Unit', blank=True),
        ),
    ]
