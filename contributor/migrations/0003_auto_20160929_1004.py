# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0002_auto_20160929_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributionsync',
            name='post_state_behind_main',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='contributionsync',
            name='post_state_uncommitted_changes',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='contributionsync',
            name='post_state_undeployed_commit',
            field=models.NullBooleanField(),
        ),
    ]
