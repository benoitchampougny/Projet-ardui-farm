# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0027_auto_20160306_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bnrdata',
            name='scale',
        ),
    ]
