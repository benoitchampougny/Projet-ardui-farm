# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0046_auto_20160311_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuatormodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='arduinomodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='boolean',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='element',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='groupfunction',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='groupfunctionmodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='optionalfunction',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='optionalfunctionmodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='pinfunction',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='raspberrymodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='shieldmodel',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
        migrations.AlterField(
            model_name='specialmeasure',
            name='version',
            field=models.FloatField(default=0.0, verbose_name=b'Version'),
        ),
    ]
