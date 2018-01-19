# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180119_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Slutt-dato'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Slutt-tidspunkt'),
        ),
    ]
