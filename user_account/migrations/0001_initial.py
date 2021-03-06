# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('inn', models.CharField(db_index=True, max_length=64, verbose_name='ИНН')),
                ('account', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='счёт')),
            ],
        ),
    ]
