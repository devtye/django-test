# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-08 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0003_auto_20160208_0551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('company_name', models.CharField(blank=True, max_length=500)),
                ('career_discription', models.TextField(blank=True)),
                ('start_date', models.DateField()),
            ],
        ),
    ]
