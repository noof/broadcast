# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0006_auto_20160202_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_text', models.CharField(max_length=200)),
            ],
        ),
    ]
