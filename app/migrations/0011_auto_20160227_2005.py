# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_notificationrequest_all_providers'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
