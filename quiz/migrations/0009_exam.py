# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151224163721 on 2015-12-27 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20151226_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('num_problems', models.IntegerField(default=0)),
            ],
        ),
    ]
