# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-28 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0004_auto_20180814_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
