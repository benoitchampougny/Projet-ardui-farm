# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0005_auto_20160131_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberry',
            name='i2cPorts',
            field=models.ManyToManyField(to='architect.I2cPort', blank=True),
        ),
    ]
