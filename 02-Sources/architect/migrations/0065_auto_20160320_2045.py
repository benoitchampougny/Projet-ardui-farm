# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0064_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name Update'),
        ),
    ]
