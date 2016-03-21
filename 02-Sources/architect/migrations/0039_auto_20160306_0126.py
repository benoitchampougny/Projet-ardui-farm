# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0038_auto_20160306_0111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupfunction',
            old_name='groupfunctionmodel',
            new_name='groupFunctionModel',
        ),
        migrations.RenameField(
            model_name='groupfunctionmodel',
            old_name='optionalfunctionmodel',
            new_name='optionalFunctionModel',
        ),
    ]
