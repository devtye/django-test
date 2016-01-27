# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 21:12
from __future__ import unicode_literals

import Addon.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('project_hook', models.IntegerField()),
                ('image_1_visibility', models.BooleanField()),
                ('image_1', models.ImageField(upload_to=Addon.models.get_upload_file_name)),
                ('discription_1', models.TextField(blank=True)),
                ('image_2_visibility', models.BooleanField()),
                ('image_2', models.ImageField(upload_to=Addon.models.get_upload_file_name)),
                ('discription_2', models.TextField(blank=True)),
                ('image_3_visibility', models.BooleanField()),
                ('image_3', models.ImageField(upload_to=Addon.models.get_upload_file_name)),
                ('discription_3', models.TextField(blank=True)),
                ('image_4_visibility', models.BooleanField()),
                ('image_4', models.ImageField(upload_to=Addon.models.get_upload_file_name)),
                ('discription_4', models.TextField(blank=True)),
            ],
        ),
    ]