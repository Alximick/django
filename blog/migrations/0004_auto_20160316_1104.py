# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_date',
            new_name='comment_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name=''),
        ),
    ]
