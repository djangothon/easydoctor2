# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_auto_20150823_0710'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('destination', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
