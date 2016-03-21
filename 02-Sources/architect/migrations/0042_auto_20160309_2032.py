# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0041_auto_20160306_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionalfunctionmodel',
            name='groupFunctionModel',
        ),
        migrations.AddField(
            model_name='groupfunctionmodel',
            name='optionalFunctionModel',
            field=models.ForeignKey(default=None, blank=True, to='architect.OptionalFunctionModel', null=True),
        ),
    ]
