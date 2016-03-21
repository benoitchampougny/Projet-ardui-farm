# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0029_auto_20160306_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='number',
            field=models.IntegerField(max_length=200),
        ),
    ]
