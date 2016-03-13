# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0026_auto_20160304_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='raspberry',
            field=models.ForeignKey(default=None, blank=True, to='architect.RaspberryModel', null=True),
        ),
    ]
