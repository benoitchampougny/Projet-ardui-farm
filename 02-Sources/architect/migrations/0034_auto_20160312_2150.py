# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0033_auto_20160312_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='sketch',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='header',
            name='sketch',
            field=models.OneToOneField(to='architect.Sketch'),
        ),
        migrations.AlterField(
            model_name='loop',
            name='sketch',
            field=models.OneToOneField(to='architect.Sketch'),
        ),
        migrations.AlterField(
            model_name='setup',
            name='sketch',
            field=models.OneToOneField(to='architect.Sketch'),
        ),
    ]
