# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usersetting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersetting',
            name='first_user',
        ),
        migrations.RemoveField(
            model_name='usersetting',
            name='last_user',
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'user_photos/', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
