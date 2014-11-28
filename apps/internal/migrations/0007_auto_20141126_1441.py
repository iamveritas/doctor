# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0006_auto_20141126_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='recommend_no',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9d\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb4\xd1\x83\xd1\x8e\xd1\x82\xd1\x8c', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='recommend_yes',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb4\xd1\x83\xd1\x8e\xd1\x82\xd1\x8c', blank=True),
            preserve_default=True,
        ),
    ]
