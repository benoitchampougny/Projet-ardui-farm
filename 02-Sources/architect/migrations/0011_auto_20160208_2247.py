# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0010_auto_20160208_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PinFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Function Name')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Function Priority')),
            ],
        ),
        migrations.AddField(
            model_name='pin',
            name='functions',
            field=models.ManyToManyField(to='architect.PinFunction'),
        ),
    ]
