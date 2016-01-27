# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0002_auto_20160127_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensormodel',
            name='sketch',
            field=models.FileField(default=None, null=True, upload_to=b'sketches/'),
        ),
    ]
