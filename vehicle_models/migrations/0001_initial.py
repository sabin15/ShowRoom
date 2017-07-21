# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_vehicle_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VRN', models.CharField(max_length=20)),
                ('VIN', models.CharField(max_length=40)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer_info')),
            ],
        ),
        migrations.CreateModel(
            name='model_first',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='model_last',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_last_name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('available_qty', models.IntegerField(default=0)),
                ('modelFirst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_models.model_first')),
            ],
        ),
        migrations.CreateModel(
            name='model_stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default='2017-07-16')),
                ('amount', models.IntegerField(default=0)),
                ('mfg_year', models.IntegerField(default=0)),
                ('modelLastId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_models.model_last')),
            ],
        ),
        migrations.AddField(
            model_name='customer_vehicle_info',
            name='model_lastId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_models.model_last'),
        ),
    ]
