# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0039_auto_20160319_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='i2cport',
            name='connection',
        ),
        migrations.DeleteModel(
            name='I2cPort',
        ),
    ]
