# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0034_auto_20160312_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatormodel',
            name='sketches',
            field=models.ManyToManyField(to='architect.Sketch'),
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='sketches',
            field=models.ManyToManyField(to='architect.Sketch'),
        ),
    ]
