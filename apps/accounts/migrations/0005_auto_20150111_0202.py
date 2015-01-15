# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150111_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersetting',
            name='first_name',
            field=models.CharField(default=11, max_length=25, verbose_name=b"\xd0\x86\xd0\xbc'\xd1\x8f", blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersetting',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 1, 11, 0, 2, 52, 897983, tzinfo=utc), max_length=30, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'user_photos/', verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb0\xd0\xb6\xd1\x82\xd0\xb5 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
