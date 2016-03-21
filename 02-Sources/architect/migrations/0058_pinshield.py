# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0057_auto_20160316_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='PinShield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200)),
                ('actuator', models.ForeignKey(default=None, blank=True, to='architect.ActuatorModel', null=True)),
                ('arduino', models.ForeignKey(default=None, blank=True, to='architect.ArduinoModel', null=True)),
                ('raspberry', models.ForeignKey(default=None, blank=True, to='architect.RaspberryModel', null=True)),
                ('sensor', models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True)),
                ('shield', models.ForeignKey(default=None, blank=True, to='architect.ShieldModel', null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
