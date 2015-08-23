# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20150823_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='illness',
        ),
        migrations.AddField(
            model_name='profile',
            name='emailId',
            field=models.EmailField(default='rashid.2008feroz@gmail.com', unique=True, max_length=30),
            preserve_default=False,
        ),
    ]
