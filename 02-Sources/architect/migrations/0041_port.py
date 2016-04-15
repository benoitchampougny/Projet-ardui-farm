# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0040_auto_20160319_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component', models.ForeignKey(to='architect.NetworkComponent')),
                ('connection', models.ManyToManyField(to='architect.Port')),
                ('pin', models.ForeignKey(related_name='ports', to='architect.Pin')),
            ],
        ),
    ]
