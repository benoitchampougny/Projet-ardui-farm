# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0030_auto_20160305_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupFunctionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Function Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Function Priority')),
                ('pin', models.ManyToManyField(to='architect.PinFunction', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OptionalFunctionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Function Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Function Priority')),
                ('pin', models.ManyToManyField(to='architect.PinFunction', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PinGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200)),
                ('actuator', models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True)),
                ('arduino', models.ForeignKey(default=None, blank=True, to='architect.ArduinoModel', null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.RemoveField(
            model_name='groupfunction',
            name='groupPin',
        ),
        migrations.RemoveField(
            model_name='groupfunction',
            name='optionalPin',
        ),
        migrations.AddField(
            model_name='groupfunction',
            name='pin',
            field=models.ManyToManyField(to='architect.Pin', blank=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='measure',
            field=models.ManyToManyField(to='architect.Measure', blank=True),
        ),
        migrations.AddField(
            model_name='pingroup',
            name='goupfunctions',
            field=models.ManyToManyField(to='architect.GroupFunction'),
        ),
        migrations.AddField(
            model_name='pingroup',
            name='raspberry',
            field=models.ForeignKey(default=None, blank=True, to='architect.RaspberryModel', null=True),
        ),
        migrations.AddField(
            model_name='pingroup',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
        migrations.AddField(
            model_name='groupfunction',
            name='groupfunctionmodel',
            field=models.ForeignKey(default=None, blank=True, to='architect.GroupFunctionModel', null=True),
        ),
        migrations.AddField(
            model_name='groupfunction',
            name='optionalfunctionmodel',
            field=models.ForeignKey(default=None, blank=True, to='architect.OptionalFunctionModel', null=True),
        ),
    ]
