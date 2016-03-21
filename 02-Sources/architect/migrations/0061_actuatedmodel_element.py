# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0060_influencemeasure'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatedmodel',
            name='element',
            field=models.ForeignKey(default=None, blank=True, to='architect.Element', null=True),
        ),
    ]
