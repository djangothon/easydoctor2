# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emailId', models.EmailField(unique=True, max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('phone', models.IntegerField(max_length=15)),
                ('address', models.TextField(max_length=60)),
            ],
        ),
    ]
