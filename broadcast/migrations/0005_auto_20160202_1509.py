# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-02 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0004_auto_20160202_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='user_api',
            new_name='groupmeapi',
        ),
    ]