# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='login.User')),
                ('travelers', models.ManyToManyField(related_name='trips', to='login.User')),
            ],
        ),
    ]
