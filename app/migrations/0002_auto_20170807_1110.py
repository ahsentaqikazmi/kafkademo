# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('numofparams', models.IntegerField()),
                ('namesofparams', models.CharField(max_length=50)),
                ('endpoints', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sensorinfo',
            },
        ),
        migrations.DeleteModel(
            name='DB',
        ),
    ]
