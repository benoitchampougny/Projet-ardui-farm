# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0015_auto_20160210_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalport',
            name='pin',
        ),
        migrations.AddField(
            model_name='digitalport',
            name='pins',
            field=models.ManyToManyField(related_name='ports', to='architect.Pin'),
        ),
    ]
