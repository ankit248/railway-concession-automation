# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0004_auto_20170319_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='sap',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
