# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drugs', '0003_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('shape', models.CharField(max_length=100)),
                ('ref_img', models.CharField(max_length=200)),
                ('imprinted_text', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('way_to_store', models.TextField()),
            ],
        ),
    ]
