# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='datatype',
            field=models.CharField(default='str', max_length=10),
            preserve_default=True,
        ),
    ]
