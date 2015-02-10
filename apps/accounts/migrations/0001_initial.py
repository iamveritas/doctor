# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDoctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('doctor', models.OneToOneField(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', error_messages={b'unique': b'\xd0\x97 \xd1\x86\xd0\xb8\xd0\xbc \xd0\xbb\xd1\x96\xd0\xba\xd0\xb0\xd1\x80\xd0\xb5\xd0\xbc \xd1\x96\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x84\xd1\x96\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe \xd1\x96\xd0\xbd\xd1\x88\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xba\xd0\xbe\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd1\x83\xd0\xb2\xd0\xb0\xd1\x87\xd0\xb0. \xd0\xaf\xd0\xba\xd1\x89\xd0\xbe \xd1\x83 \xd0\x92\xd0\xb0\xd1\x81 \xd0\xb2\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb8 \xd0\xbf\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f, \xd0\xb7\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbd\xd1\x96\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xb4\xd0\xbe \xd0\xb0\xd0\xb4\xd0\xbc\xd1\x96\xd0\xbd\xd1\x96\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd1\x83.'}, to='internal.Doctor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.TextField()),
                ('user', models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5', blank=True)),
                ('first_name', models.CharField(max_length=25, verbose_name=b"\xd0\x86\xd0\xbc'\xd1\x8f", blank=True)),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'user_photos/', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd1\x96\xd1\x8f', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
