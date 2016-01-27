# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Interface Type Name')),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1)),
                ('interfaceType', models.ForeignKey(default=None, blank=True, to='architect.InterfaceType', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='source',
            field=models.ForeignKey(related_name='target', default=None, blank=True, to='architect.Port', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='target',
            field=models.ForeignKey(related_name='source', default=None, blank=True, to='architect.Port', null=True),
        ),
    ]
