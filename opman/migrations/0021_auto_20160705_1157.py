# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0020_auto_20160704_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='fullname',
            field=models.CharField(default=None, max_length=64, null=True, unique=True, verbose_name='姓名'),
        ),
    ]
