# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('run_id', models.IntegerField(serialize=False, primary_key=True)),
                ('team_id', models.CharField(max_length=8)),
                ('pid', models.CharField(max_length=8)),
                ('result', models.CharField(max_length=64)),
                ('time', models.DateTimeField()),
                ('ip', models.CharField(max_length=64)),
                ('output', models.CharField(max_length=255)),
                ('solution', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
