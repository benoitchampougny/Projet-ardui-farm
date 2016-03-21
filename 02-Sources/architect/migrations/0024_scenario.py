# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import architect.models.Location


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0023_auto_20160228_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Scenario Name')),
                ('locationPorts', models.ManyToManyField(to='architect.LocationPort', blank=True)),
            ],
            bases=(models.Model, architect.models.Location.LocationComponent),
        ),
    ]
