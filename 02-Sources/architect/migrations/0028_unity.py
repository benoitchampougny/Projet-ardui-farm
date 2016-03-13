# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0027_pin_raspberry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Unity Name')),
                ('sensor', models.ForeignKey(default=None, blank=True, to='architect.Measure', null=True)),
            ],
        ),
    ]
