# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='part_processing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_date', models.DateField(default='2017-07-13')),
                ('pID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.part_list')),
            ],
        ),
        migrations.RemoveField(
            model_name='part_stock',
            name='remaining',
        ),
    ]
