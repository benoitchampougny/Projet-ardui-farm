# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import architect.models.Location


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0021_message_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Location Name')),
            ],
            bases=(models.Model, architect.models.Location.LocationComponent),
        ),
        migrations.CreateModel(
            name='LocationPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(default=b'DW', max_length=2, choices=[(b'UP', b'Upward'), (b'DW', b'Downward')])),
                ('address', models.CharField(default=None, max_length=200, null=True, verbose_name=b'Address', blank=True)),
                ('connection', models.ManyToManyField(related_name='connection_rel_+', to='architect.LocationPort', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Location Name')),
                ('locationPorts', models.ManyToManyField(to='architect.LocationPort', blank=True)),
            ],
            bases=(models.Model, architect.models.Location.LocationComponent),
        ),
        migrations.RemoveField(
            model_name='measure',
            name='sensor',
        ),
        migrations.RemoveField(
            model_name='measure',
            name='technicalElement',
        ),
        migrations.RemoveField(
            model_name='technicalelement',
            name='location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='inside',
        ),
        migrations.DeleteModel(
            name='Measure',
        ),
        migrations.DeleteModel(
            name='TechnicalElement',
        ),
        migrations.AddField(
            model_name='environment',
            name='locationPorts',
            field=models.ManyToManyField(to='architect.LocationPort', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='master',
            field=models.ForeignKey(default=None, blank=True, to='architect.Environment', null=True),
        ),
    ]
