# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0040_auto_20160306_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='optionalfunctionmodel',
            old_name='groupfunctionmodel',
            new_name='groupFunctionModel',
        ),
    ]
