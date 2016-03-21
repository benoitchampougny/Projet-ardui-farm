# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0025_auto_20160304_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinfunction',
            name='shortName',
        ),
        migrations.AddField(
            model_name='pinfunction',
            name='detail',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'detail'),
        ),
    ]
