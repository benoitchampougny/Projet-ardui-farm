# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0025_auto_20160304_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='BNR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lsb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('msb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('scale', models.DecimalField(default=1, max_digits=7, decimal_places=2)),
                ('minValue', models.IntegerField(null=True, blank=True)),
                ('maxValue', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['lsb'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discrete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lsb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('msb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('trueName', models.CharField(max_length=100, null=True)),
                ('falseName', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['lsb'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='bcddata',
            name='scale',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sdi',
        ),
        migrations.RemoveField(
            model_name='message',
            name='ssm',
        ),
        migrations.RemoveField(
            model_name='sensormodel',
            name='sketch',
        ),
        migrations.AddField(
            model_name='actuatormodel',
            name='suscribe',
            field=models.ManyToManyField(to='architect.Message', blank=True),
        ),
        migrations.AddField(
            model_name='bcddata',
            name='maxValue',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bcddata',
            name='minValue',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='publish',
            field=models.ManyToManyField(to='architect.Message', blank=True),
        ),
        migrations.AddField(
            model_name='discrete',
            name='message',
            field=models.ForeignKey(to='architect.Message'),
        ),
        migrations.AddField(
            model_name='bnr',
            name='message',
            field=models.ForeignKey(to='architect.Message'),
        ),
        migrations.AddField(
            model_name='bnr',
            name='units',
            field=models.ForeignKey(default=None, blank=True, to='architect.Units', null=True),
        ),
    ]
