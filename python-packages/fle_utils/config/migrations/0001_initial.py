# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('value', models.TextField(blank=True)),
                ('datatype', models.CharField(default=b'str', max_length=10)),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
            bases=(models.Model,),
        ),
    ]
