# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-06-02 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nemo', '0002_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
