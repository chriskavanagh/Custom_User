# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 04:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20160304_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
    ]
