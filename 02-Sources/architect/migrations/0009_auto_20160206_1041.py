# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0008_auto_20160203_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(default=b'DW', max_length=2, choices=[(b'UP', b'Upward'), (b'DW', b'Downward')])),
                ('address', models.CharField(default=None, max_length=200, verbose_name=b'Address', blank=True)),
                ('connection', models.ManyToManyField(related_name='connection_rel_+', to='architect.DigitalPort', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='wifiport',
            name='number',
        ),
        migrations.AddField(
            model_name='wifiport',
            name='direction',
            field=models.CharField(default=b'DW', max_length=2, choices=[(b'UP', b'Upward'), (b'DW', b'Downward')]),
        ),
        migrations.AlterField(
            model_name='i2cport',
            name='address',
            field=models.CharField(default=None, max_length=200, verbose_name=b'Address', blank=True),
        ),
        migrations.AlterField(
            model_name='wifiport',
            name='address',
            field=models.CharField(default=None, max_length=200, verbose_name=b'Address', blank=True),
        ),
    ]
