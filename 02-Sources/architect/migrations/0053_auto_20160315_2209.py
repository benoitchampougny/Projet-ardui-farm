# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0052_auto_20160315_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pingroup',
            old_name='goupFunctionModel',
            new_name='groupFunctionModel',
        ),
    ]
