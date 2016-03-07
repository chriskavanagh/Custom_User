# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0005_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
