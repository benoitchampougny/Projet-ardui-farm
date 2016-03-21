# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0062_actuatedmodel_flowactuator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technicalcaracteristic',
            options={'ordering': ['actuated']},
        ),
    ]
