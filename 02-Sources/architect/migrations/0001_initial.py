# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
    ]
