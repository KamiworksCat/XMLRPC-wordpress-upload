# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolt_usersite', '0002_auto_20160426_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='bolt_usersite.Tags'),
        ),
    ]