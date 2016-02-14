# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0014_auto_20160210_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='sensor',
            field=models.ForeignKey(default=None, blank=True, to='architect.SensorModel', null=True),
        ),
        migrations.AlterField(
            model_name='actuatormodel',
            name='sketch',
            field=models.FileField(null=True, upload_to=b'sketches/', blank=True),
        ),
        migrations.RemoveField(
            model_name='digitalport',
            name='pin',
        ),
        migrations.AddField(
            model_name='digitalport',
            name='pin',
            field=models.ManyToManyField(to='architect.Pin'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='arduino',
            field=models.ForeignKey(default=None, blank=True, to='architect.ArduinoModel', null=True),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='sketch',
            field=models.FileField(null=True, upload_to=b'sketches/', blank=True),
        ),
    ]
