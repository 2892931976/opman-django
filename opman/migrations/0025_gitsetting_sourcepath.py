# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0024_auto_20160711_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitsetting',
            name='sourcepath',
            field=models.CharField(default=None, max_length=50, null=True, unique=True, verbose_name='源目录'),
        ),
    ]
