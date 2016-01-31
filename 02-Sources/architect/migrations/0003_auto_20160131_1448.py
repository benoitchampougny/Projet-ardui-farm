# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0002_auto_20160130_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i2cport',
            name='address',
            field=models.CharField(default=None, max_length=200, verbose_name=b'I2C Address', blank=True),
        ),
        migrations.AlterField(
            model_name='wifiport',
            name='address',
            field=models.CharField(default=None, max_length=200, verbose_name=b'IP Address', blank=True),
        ),
        migrations.AlterField(
            model_name='wifiport',
            name='password',
            field=models.CharField(default=None, max_length=200, verbose_name=b'Password', blank=True),
        ),
        migrations.AlterField(
            model_name='wifiport',
            name='port',
            field=models.IntegerField(default=8000, verbose_name=b'UDP Port', blank=True),
        ),
    ]
