# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0054_auto_20160316_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensormodel',
            name='boolean',
            field=models.ManyToManyField(to='architect.Boolean', blank=True),
        ),
    ]
