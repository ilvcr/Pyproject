# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0004_auto_20160712_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='upstream_config',
            name='port',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proxy_config',
            name='protocols',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='proxy_config',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='upstream_config',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
