# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0063_auto_20160320_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Special Measure Name')),
                ('version', models.FloatField(default=0.0, verbose_name=b'Version')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
