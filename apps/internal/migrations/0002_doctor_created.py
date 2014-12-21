# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 18, 14, 9, 32, 682447, tzinfo=utc), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd1\x82\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', auto_now_add=True),
            preserve_default=False,
        ),
    ]
