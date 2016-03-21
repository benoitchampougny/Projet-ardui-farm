# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0028_remove_bnrdata_scale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnrdata',
            name='maxValue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bnrdata',
            name='minValue',
            field=models.IntegerField(),
        ),
    ]
