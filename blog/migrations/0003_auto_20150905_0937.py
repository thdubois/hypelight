# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
