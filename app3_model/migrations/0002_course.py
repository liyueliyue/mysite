# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-04-14 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=64)),
                ('teacher', models.CharField(max_length=25)),
                ('score', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
