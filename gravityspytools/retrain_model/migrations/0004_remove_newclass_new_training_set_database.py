# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-30 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retrain_model', '0003_newclass_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newclass',
            name='new_training_set_database',
        ),
    ]
