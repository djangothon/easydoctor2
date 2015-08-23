# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20150823_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emailId',
            field=models.EmailField(max_length=30),
        ),
    ]
