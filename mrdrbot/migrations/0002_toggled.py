# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrdrbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toggled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onstatus', models.BooleanField(default=False)),
            ],
        ),
    ]
