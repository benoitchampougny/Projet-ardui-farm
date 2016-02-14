# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0016_auto_20160210_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalport',
            name='pwm',
        ),
        migrations.AlterField(
            model_name='digitalport',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Address', blank=True),
        ),
        migrations.AlterField(
            model_name='i2cport',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Address', blank=True),
        ),
        migrations.AlterField(
            model_name='wifiport',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Address', blank=True),
        ),
    ]
