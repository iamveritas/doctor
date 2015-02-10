# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0006_auto_20150102_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bribery',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Bribery',
        ),
        migrations.RemoveField(
            model_name='efficiency',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Efficiency',
        ),
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.RemoveField(
            model_name='quality',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Quality',
        ),
        migrations.RemoveField(
            model_name='respect',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Respect',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'doctor_photos/', verbose_name=b'\xd0\x97\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', blank=True),
            preserve_default=True,
        ),
    ]
