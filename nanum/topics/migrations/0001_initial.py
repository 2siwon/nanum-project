# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='topic')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
