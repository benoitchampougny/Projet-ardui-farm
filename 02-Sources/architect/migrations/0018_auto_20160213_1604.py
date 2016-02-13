# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('architect', '0017_auto_20160210_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='BCDData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lsb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('msb', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(29)])),
                ('scale', models.DecimalField(default=1, max_digits=7, decimal_places=2)),
                ('decimalPlaces', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['lsb'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.IntegerField(validators=[django.core.validators.MaxValueValidator(255)])),
                ('sdi', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3)])),
                ('ssm', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='bcddata',
            name='message',
            field=models.ForeignKey(to='architect.Message'),
        ),
        migrations.AddField(
            model_name='bcddata',
            name='units',
            field=models.ForeignKey(default=None, blank=True, to='architect.Units', null=True),
        ),
    ]
