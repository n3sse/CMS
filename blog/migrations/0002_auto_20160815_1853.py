# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-nick'], 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published_date'], 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]