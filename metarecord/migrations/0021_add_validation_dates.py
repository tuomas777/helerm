# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-06 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0020_add_attribute_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid to'),
        ),
        migrations.AddField(
            model_name='function',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AddField(
            model_name='metadataversion',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid to'),
        ),
        migrations.AddField(
            model_name='metadataversion',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
    ]
