# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20161105_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisis',
            name='closed',
            field=models.BooleanField(default='False'),
        ),
    ]
