# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0019_auto_20160630_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kaoqin',
            name='leave',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='请假时间'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='fullname',
            field=models.CharField(default=None, max_length=64, unique=True, verbose_name='姓名'),
        ),
    ]
