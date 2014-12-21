# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('perm', models.CharField(max_length=8)),
                ('senior', models.IntegerField()),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problemset',
            fields=[
                ('pid', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('score', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('differ', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'problemset',
                'managed': False,
            },
            bases=(models.Model,),
        ),
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
