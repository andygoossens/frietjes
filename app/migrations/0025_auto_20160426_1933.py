# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-26 19:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_userinvite'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvite',
            name='used_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 19, 33, 16, 584759, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='secret',
            field=models.CharField(editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]
