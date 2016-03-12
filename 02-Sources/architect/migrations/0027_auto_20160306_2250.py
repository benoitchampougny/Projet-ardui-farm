# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0026_auto_20160306_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='BNRData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lsb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('msb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('scale', models.DecimalField(default=1, max_digits=7, decimal_places=2)),
                ('minValue', models.IntegerField(null=True, blank=True)),
                ('maxValue', models.IntegerField(null=True, blank=True)),
                ('message', models.ForeignKey(to='architect.Message')),
                ('units', models.ForeignKey(default=None, blank=True, to='architect.Units', null=True)),
            ],
            options={
                'ordering': ['lsb'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiscreteData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lsb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('msb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('trueName', models.CharField(max_length=100, null=True)),
                ('falseName', models.CharField(max_length=100, null=True)),
                ('message', models.ForeignKey(to='architect.Message')),
            ],
            options={
                'ordering': ['lsb'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='bnr',
            name='message',
        ),
        migrations.RemoveField(
            model_name='bnr',
            name='units',
        ),
        migrations.RemoveField(
            model_name='discrete',
            name='message',
        ),
        migrations.DeleteModel(
            name='BNR',
        ),
        migrations.DeleteModel(
            name='Discrete',
        ),
    ]
