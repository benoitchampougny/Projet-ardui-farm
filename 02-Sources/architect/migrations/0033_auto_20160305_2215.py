# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0032_auto_20160305_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionalfunctionmodel',
            name='pin',
        ),
        migrations.AddField(
            model_name='pinfunction',
            name='optionalfunctionmodel',
            field=models.ManyToManyField(to='architect.OptionalFunctionModel', blank=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Unit Name'),
        ),
    ]
