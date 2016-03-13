# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0032_auto_20160306_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sketch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='setup',
            name='sketch',
            field=models.ForeignKey(to='architect.Sketch'),
        ),
        migrations.AddField(
            model_name='loop',
            name='sketch',
            field=models.ForeignKey(to='architect.Sketch'),
        ),
        migrations.AddField(
            model_name='header',
            name='sketch',
            field=models.ForeignKey(to='architect.Sketch'),
        ),
        migrations.AddField(
            model_name='arduinomodel',
            name='sketches',
            field=models.ManyToManyField(to='architect.Sketch'),
        ),
    ]
