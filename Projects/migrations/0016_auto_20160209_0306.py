# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 03:06
from __future__ import unicode_literals

import Projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0015_auto_20160209_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='header',
            field=models.FileField(blank=True, upload_to=Projects.models.get_upload_file_name),
        ),
    ]
