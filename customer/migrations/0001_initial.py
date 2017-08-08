# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('add_city', models.CharField(max_length=50)),
                ('add_dist', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
            ],
        ),
    ]
