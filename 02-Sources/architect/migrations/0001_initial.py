# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Card Name')),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Model Name')),
                ('sketch', models.FileField(default=None, null=True, upload_to=b'sketches/')),
            ],
        ),
        migrations.CreateModel(
            name='Arduino',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Card Name')),
            ],
        ),
        migrations.CreateModel(
            name='ArduinoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Model Name')),
                ('ioPins', models.IntegerField(default=0, verbose_name=b'Digital I/O Pins')),
                ('pwmPins', models.IntegerField(default=0, verbose_name=b'PWM Digital I/O Pins')),
                ('analogIn', models.IntegerField(default=0, verbose_name=b'Analog Input Pins')),
            ],
        ),
        migrations.CreateModel(
            name='I2cPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1, verbose_name=b'Number')),
                ('address', models.CharField(max_length=200, verbose_name=b'I2C Address')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Location Name')),
                ('inside', models.ForeignKey(related_name='contain', to='architect.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Measure Name')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Network Name')),
            ],
        ),
        migrations.CreateModel(
            name='Raspberry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Card Name')),
            ],
        ),
        migrations.CreateModel(
            name='RaspberryModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Model Name')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Card Name')),
            ],
        ),
        migrations.CreateModel(
            name='SensorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Model Name')),
                ('sketch', models.FileField(default=None, null=True, upload_to=b'sketches/')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Technical Element Name')),
                ('location', models.ForeignKey(default=None, blank=True, to='architect.Location', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WifiPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1, verbose_name=b'Number')),
                ('address', models.CharField(max_length=200, verbose_name=b'IP Address')),
                ('port', models.IntegerField(default=8000, verbose_name=b'UDP Port')),
                ('password', models.CharField(max_length=200, verbose_name=b'Password')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='cardModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
        migrations.AddField(
            model_name='raspberry',
            name='cardModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.RaspberryModel', null=True),
        ),
        migrations.AddField(
            model_name='raspberry',
            name='i2cPorts',
            field=models.ManyToManyField(to='architect.I2cPort'),
        ),
        migrations.AddField(
            model_name='raspberry',
            name='wifiPorts',
            field=models.ManyToManyField(to='architect.WifiPort'),
        ),
        migrations.AddField(
            model_name='network',
            name='master',
            field=models.ForeignKey(default=None, blank=True, to='architect.Raspberry', null=True),
        ),
        migrations.AddField(
            model_name='measure',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.Sensor', null=True),
        ),
        migrations.AddField(
            model_name='measure',
            name='technicalElement',
            field=models.ForeignKey(default=None, blank=True, to='architect.TechnicalElement', null=True),
        ),
        migrations.AddField(
            model_name='arduino',
            name='cardModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.ArduinoModel', null=True),
        ),
        migrations.AddField(
            model_name='arduino',
            name='i2cPorts',
            field=models.ManyToManyField(to='architect.I2cPort'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='cardModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
    ]
