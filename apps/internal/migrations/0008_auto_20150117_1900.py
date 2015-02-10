# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0007_auto_20150117_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='patronymic',
            field=models.CharField(max_length=30, verbose_name=b'\xd0\x9f\xd0\xbe \xd0\xb1\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96', blank=True),
            preserve_default=True,
        ),
    ]
