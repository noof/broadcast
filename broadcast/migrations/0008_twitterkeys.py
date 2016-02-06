# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0007_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_key', models.CharField(max_length=200)),
                ('consumer_secret', models.CharField(max_length=200)),
                ('access_token_key', models.CharField(max_length=200)),
                ('access_token_secret', models.CharField(max_length=200)),
            ],
        ),
    ]
