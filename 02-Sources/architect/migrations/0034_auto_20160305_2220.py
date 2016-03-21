# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0033_auto_20160305_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinfunction',
            name='optionalfunctionmodel',
        ),
        migrations.AddField(
            model_name='optionalfunctionmodel',
            name='pinfunction',
            field=models.ManyToManyField(to='architect.PinFunction', blank=True),
        ),
    ]
