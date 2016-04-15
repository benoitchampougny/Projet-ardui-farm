# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0036_auto_20160319_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkcomponent',
            name='dioConnection',
            field=models.ForeignKey(related_name='dioSubComponent', default=None, blank=True, to='architect.NetworkComponent', null=True),
        ),
        migrations.AlterField(
            model_name='networkcomponent',
            name='i2cConnection',
            field=models.ForeignKey(related_name='i2cSubComponent', default=None, blank=True, to='architect.NetworkComponent', null=True),
        ),
        migrations.AlterField(
            model_name='networkcomponent',
            name='wifiConnection',
            field=models.ForeignKey(related_name='wifiSubComponent', default=None, blank=True, to='architect.NetworkComponent', null=True),
        ),
    ]
