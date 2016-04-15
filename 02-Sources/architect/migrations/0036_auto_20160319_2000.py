# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0035_auto_20160312_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dioConnection', models.ForeignKey(related_name='dioSubComponent', to='architect.NetworkComponent')),
                ('i2cConnection', models.ForeignKey(related_name='i2cSubComponent', to='architect.NetworkComponent')),
                ('wifiConnection', models.ForeignKey(related_name='wifiSubComponent', to='architect.NetworkComponent')),
            ],
        ),
        migrations.RemoveField(
            model_name='actuator',
            name='id',
        ),
        migrations.RemoveField(
            model_name='arduino',
            name='id',
        ),
        migrations.RemoveField(
            model_name='raspberry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='id',
        ),
        migrations.AddField(
            model_name='actuator',
            name='networkcomponent_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='architect.NetworkComponent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arduino',
            name='networkcomponent_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='architect.NetworkComponent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raspberry',
            name='networkcomponent_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='architect.NetworkComponent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='networkcomponent_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='architect.NetworkComponent'),
            preserve_default=False,
        ),
    ]
