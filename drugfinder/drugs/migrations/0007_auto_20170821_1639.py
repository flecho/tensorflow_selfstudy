# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0006_auto_20170821_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='dosage',
            field=models.TextField(null=True),
        ),
    ]