# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_auto_20141031_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='is_active',
            field=models.CharField(default=False, max_length=5, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81', choices=[(b'False', b'\xd0\xbd\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb8\xd0\xb9'), (b'True', b'\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb8\xd0\xb9')]),
            preserve_default=True,
        ),
    ]
