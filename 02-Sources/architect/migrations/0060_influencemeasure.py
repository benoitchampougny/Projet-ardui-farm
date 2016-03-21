# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0059_actuatedmodel_technicalcaracteristic'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluenceMeasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=200, verbose_name=b'Direction')),
                ('actuated', models.ForeignKey(default=None, blank=True, to='architect.ActuatedModel', null=True)),
                ('measure', models.ForeignKey(default=None, blank=True, to='architect.Measure', null=True)),
            ],
        ),
    ]
