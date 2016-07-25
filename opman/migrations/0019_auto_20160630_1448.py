# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0018_auto_20160630_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kaoqin',
            name='late',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='迟到时间'),
        ),
        migrations.AlterField(
            model_name='kaoqin',
            name='plus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='加班时间'),
        ),
    ]
