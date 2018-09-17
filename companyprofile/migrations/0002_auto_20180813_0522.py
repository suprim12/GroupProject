# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-12 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='/company'),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]