# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrisisMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inCrisis', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='crisis',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crisis',
            name='severity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crisis',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
