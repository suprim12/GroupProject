# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-04 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeprofile', '0004_employeeprofile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
