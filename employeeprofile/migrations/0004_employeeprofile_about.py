# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-04 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeprofile', '0003_employeeprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
