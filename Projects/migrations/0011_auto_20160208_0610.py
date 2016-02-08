# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-08 06:10
from __future__ import unicode_literals

import Projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0010_auto_20160208_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='header',
            field=models.FileField(blank=True, upload_to=Projects.models.get_upload_file_name),
        ),
    ]