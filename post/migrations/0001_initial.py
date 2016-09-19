# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=140)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
