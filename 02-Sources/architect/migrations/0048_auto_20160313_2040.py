# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0047_auto_20160313_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatormodel',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='boolean',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='element',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='groupfunction',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='groupfunctionmodel',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='measure',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='optionalfunction',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='optionalfunctionmodel',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='pinfunction',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='raspberrymodel',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='sensormodel',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='shieldmodel',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
        migrations.AddField(
            model_name='specialmeasure',
            name='lastVersion',
            field=models.BooleanField(default=True, verbose_name=b'Last Version'),
        ),
    ]
