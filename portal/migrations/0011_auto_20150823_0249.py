# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='emailId',
            field=models.EmailField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emailId',
            field=models.EmailField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='emailId',
            field=models.EmailField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
