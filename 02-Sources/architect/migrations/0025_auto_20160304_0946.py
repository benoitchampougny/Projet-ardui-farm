# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0024_scenario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Boolean Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('true', models.CharField(max_length=200, verbose_name=b'True')),
                ('false', models.CharField(max_length=200, verbose_name=b'False')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Element Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
            ],
        ),
        migrations.CreateModel(
            name='GroupFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Function Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Function Priority')),
            ],
        ),
        migrations.CreateModel(
            name='I2cAdress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'I2c Adress Name')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Measure Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('nameUnity', models.CharField(max_length=200, verbose_name=b'Unity Of Measue')),
            ],
        ),
        migrations.CreateModel(
            name='OptionalFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Function Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Function Priority')),
            ],
        ),
        migrations.CreateModel(
            name='ShieldModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Model Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialMeasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Special Measure Name')),
                ('version', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version')),
                ('specialUnity', models.CharField(max_length=200, verbose_name=b'Special Unity')),
            ],
        ),
        migrations.AddField(
            model_name='actuatormodel',
            name='version',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version'),
        ),
        migrations.AddField(
            model_name='arduinomodel',
            name='version',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version'),
        ),
        migrations.AddField(
            model_name='pinfunction',
            name='shortName',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Function Short Name'),
        ),
        migrations.AddField(
            model_name='pinfunction',
            name='version',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version'),
        ),
        migrations.AddField(
            model_name='raspberrymodel',
            name='version',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version'),
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='version',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='number',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='optionalfunction',
            name='optionalPin',
            field=models.ForeignKey(to='architect.PinFunction', max_length=200),
        ),
        migrations.AddField(
            model_name='measure',
            name='actuator',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
        migrations.AddField(
            model_name='measure',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
        migrations.AddField(
            model_name='i2cadress',
            name='actuator',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
        migrations.AddField(
            model_name='i2cadress',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
        migrations.AddField(
            model_name='groupfunction',
            name='groupPin',
            field=models.ForeignKey(default=None, to='architect.PinFunction', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='groupfunction',
            name='optionalPin',
            field=models.ForeignKey(default=None, to='architect.OptionalFunction', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='element',
            name='actuator',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
        migrations.AddField(
            model_name='element',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
        migrations.AddField(
            model_name='boolean',
            name='actuator',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
        migrations.AddField(
            model_name='boolean',
            name='element',
            field=models.ForeignKey(to='architect.Element', max_length=200),
        ),
        migrations.AddField(
            model_name='boolean',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
    ]
