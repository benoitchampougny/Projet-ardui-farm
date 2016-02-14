# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0013_auto_20160208_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pin',
            options={'ordering': ['number']},
        ),
        migrations.AddField(
            model_name='digitalport',
            name='pin',
            field=models.ForeignKey(default=1, to='architect.Pin'),
            preserve_default=False,
        ),
    ]
