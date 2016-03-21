# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0031_auto_20160305_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupfunction',
            name='optionalfunctionmodel',
        ),
        migrations.AddField(
            model_name='groupfunctionmodel',
            name='optionalfunctionmodel',
            field=models.ForeignKey(default=None, blank=True, to='architect.OptionalFunctionModel', null=True),
        ),
    ]
