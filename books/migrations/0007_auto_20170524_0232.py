# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default=-111, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='value', max_length=1000),
            preserve_default=False,
        ),
    ]