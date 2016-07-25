# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 08:39
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(max_length=2, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField()),
                ('appname', models.CharField(max_length=15, verbose_name='应用名字')),
            ],
        ),
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcinfo', models.CharField(max_length=100, verbose_name='机房')),
                ('ipinfo', models.GenericIPAddressField(verbose_name='主机IP')),
                ('repairinfo', models.IntegerField(verbose_name='维修状态')),
                ('brandinfo', models.CharField(max_length=15, verbose_name='品牌')),
                ('buytime', models.DateField(verbose_name='购买日期')),
                ('hostname', models.CharField(max_length=50, verbose_name='主机名')),
                ('osinfo', models.CharField(max_length=50, verbose_name='系统版本')),
                ('modelinfo', models.CharField(max_length=50, verbose_name='型号')),
                ('memoryinfo', models.CharField(max_length=15, verbose_name='内存信息')),
                ('diskinfo', models.CharField(max_length=50, verbose_name='硬盘信息')),
                ('cpuinfo', models.CharField(max_length=50, verbose_name='CPU信息')),
                ('snnum', models.CharField(max_length=30, verbose_name='服务编号')),
                ('usefor', models.CharField(max_length=80, verbose_name='用途')),
                ('status', models.IntegerField(default=None, verbose_name='是否在用')),
            ],
        ),
        migrations.CreateModel(
            name='IdcList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcname', models.CharField(max_length=20, verbose_name='合作商')),
                ('cityname', models.CharField(max_length=5, verbose_name='所在城市')),
                ('position', models.CharField(max_length=20, verbose_name='地理位置')),
                ('hostnum', models.IntegerField()),
                ('bandwidth', models.IntegerField()),
                ('expense', models.IntegerField()),
                ('starttime', models.DateField(verbose_name='开始时间')),
                ('iphonecall', models.CharField(max_length=20, verbose_name='值班电话')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PermissonList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RepairInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField()),
                ('starttime', models.TimeField()),
                ('badinfo', models.CharField(max_length=100, verbose_name='损坏信息')),
                ('repairmethod', models.CharField(max_length=100, verbose_name='维修方案')),
                ('endtime', models.TimeField()),
                ('costifno', models.CharField(max_length=50, verbose_name='维修费用')),
            ],
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('permission', models.ManyToManyField(blank=True, to='opman.PermissonList')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opman.RoleList'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
