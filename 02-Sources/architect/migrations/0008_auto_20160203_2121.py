# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0007_auto_20160131_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='i2cport',
            name='number',
        ),
    ]
