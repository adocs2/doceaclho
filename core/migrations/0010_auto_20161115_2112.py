# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-15 23:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161115_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='intro',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]