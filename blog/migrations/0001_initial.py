# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
