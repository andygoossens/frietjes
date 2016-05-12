# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-25 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_company_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Company'),
            preserve_default=False,
        ),
    ]