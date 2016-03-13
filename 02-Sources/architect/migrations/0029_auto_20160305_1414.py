# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0028_unity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unity',
            new_name='Unit',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='sensor',
            new_name='measure',
        ),
        migrations.RemoveField(
            model_name='measure',
            name='nameUnity',
        ),
    ]
