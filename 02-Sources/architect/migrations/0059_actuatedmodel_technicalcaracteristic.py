# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0058_pinshield'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActuatedModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Model Name')),
                ('brand', models.CharField(max_length=200, verbose_name=b'Brand')),
                ('version', models.FloatField(default=0.0, verbose_name=b'Version')),
                ('lastVersion', models.BooleanField(default=True, verbose_name=b'Last Version')),
            ],
        ),
        migrations.CreateModel(
            name='technicalCaracteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=0.0, verbose_name=b'Value')),
                ('actuated', models.ForeignKey(default=None, blank=True, to='architect.ActuatedModel', null=True)),
                ('measure', models.ForeignKey(default=None, blank=True, to='architect.Measure', null=True)),
                ('unit', models.ForeignKey(default=None, blank=True, to='architect.Unit', null=True)),
            ],
        ),
    ]
