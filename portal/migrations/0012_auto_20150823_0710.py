# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20150823_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctorEmail',
            field=models.EmailField(default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientEmail',
            field=models.EmailField(default='None', max_length=30),
            preserve_default=False,
        ),
    ]
