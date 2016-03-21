# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0035_auto_20160305_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupfunctionmodel',
            old_name='optionalfunctionmodel',
            new_name='optionalFunctionModel',
        ),
    ]
