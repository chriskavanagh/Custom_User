# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-10 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0009_usersession'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]