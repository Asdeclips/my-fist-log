# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribute', '0002_auto_20160813_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='palette',
            field=models.TextField(null=True, blank=True, max_length=200),
        ),
    ]
