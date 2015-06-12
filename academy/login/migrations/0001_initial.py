# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetAudit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=75)),
                ('request_date', models.DateField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Password reset audit',
                'ordering': ['-modified'],
                'verbose_name': 'Password reset audit',
            },
            bases=(models.Model,),
        ),
    ]
