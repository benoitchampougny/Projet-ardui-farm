# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0037_auto_20160306_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupfunctionmodel',
            old_name='optionalfunctiomodel',
            new_name='optionalfunctionmodel',
        ),
    ]
