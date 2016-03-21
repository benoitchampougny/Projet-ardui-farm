# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0034_auto_20160305_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupfunctionmodel',
            old_name='pin',
            new_name='pinfunction',
        ),
    ]
