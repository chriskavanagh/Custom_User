# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0006_auto_20160305_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]