# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-01-25 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kolibri_instant_schools_plugin', '0004_auto_20220331_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField()),
                ('kind', models.TextField(choices=[('FAQ', 'FAQ'), ('About', 'About')])),
            ],
        ),
    ]
