# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-19 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_auto_20200219_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilefeeditem',
            name='user_profil',
        ),
        migrations.AddField(
            model_name='profilefeeditem',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
