# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_auto_20141222_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'doctor_photos/', null=True, verbose_name=b'\xd0\x97\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', blank=True),
            preserve_default=True,
        ),
    ]
