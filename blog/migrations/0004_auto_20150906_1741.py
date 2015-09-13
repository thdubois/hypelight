# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150905_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='url',
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 9, 6, 17, 41, 45, 635275, tzinfo=utc), max_length=200, upload_to=b'img'),
            preserve_default=False,
        ),
    ]
