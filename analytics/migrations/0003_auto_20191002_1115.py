# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-02 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20191002_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdata',
            name='status_for_reporting',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='masterdata',
            name='utility',
            field=models.CharField(max_length=60),
        ),
    ]
