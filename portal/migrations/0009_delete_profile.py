# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20150823_0132'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile',
        ),
    ]
