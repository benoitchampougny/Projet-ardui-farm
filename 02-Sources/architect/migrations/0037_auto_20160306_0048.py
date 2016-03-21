# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0036_auto_20160306_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupfunctionmodel',
            old_name='optionalFunctionModel',
            new_name='optionalfunctiomodel',
        ),
    ]
