# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-14 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0003_auto_20180814_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='company',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='/company'),
        ),
    ]
