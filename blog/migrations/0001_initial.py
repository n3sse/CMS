# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nick', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-nick'],
                'verbose_name_plural': ['Authors'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('tags', models.CharField(max_length=128)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField()),
                ('approved', models.BooleanField(default=False)),
                ('views', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
            ],
            options={
                'ordering': ['published_date'],
                'verbose_name_plural': ['Posts'],
            },
        ),
    ]
