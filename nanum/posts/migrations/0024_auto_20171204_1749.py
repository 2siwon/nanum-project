# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20171204_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='downvote_count',
            new_name='follow_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvote_count',
        ),
    ]
