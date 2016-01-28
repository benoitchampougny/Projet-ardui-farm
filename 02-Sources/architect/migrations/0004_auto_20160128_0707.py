# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0003_sensormodel_sketch'),
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
            name='I2cPort',
            fields=[
                ('port_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='architect.Port')),
                ('address', models.CharField(max_length=200, verbose_name=b'I2C Address')),
            ],
            bases=('architect.port',),
        ),
        migrations.CreateModel(
            name='WifiPort',
            fields=[
                ('port_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='architect.Port')),
                ('address', models.IntegerField(verbose_name=b'UDP Port')),
                ('password', models.CharField(max_length=200, verbose_name=b'Password')),
            ],
            bases=('architect.port',),
        ),
        migrations.RemoveField(
            model_name='port',
            name='interfaceType',
        ),
        migrations.DeleteModel(
            name='InterfaceType',
        ),
        migrations.AddField(
            model_name='actuator',
            name='cardModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True),
        ),
        migrations.AddField(
            model_name='arduino',
            name='i2cPorts',
            field=models.ManyToManyField(to='architect.I2cPort'),
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
    ]
