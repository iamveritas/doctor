# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internal', '0004_auto_20141031_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommendation', models.BooleanField()),
                ('doctor', models.ForeignKey(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', to='internal.Doctor')),
                ('user', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd1\x83\xd0\xb2\xd0\xb0\xd1\x87', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0456\u0457 \u043f\u0430\u0446\u0456\u0454\u043d\u0442\u0456\u0432',
                'verbose_name_plural': '\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0456\u0457 \u043f\u0430\u0446\u0456\u0454\u043d\u0442\u0456\u0432',
            },
            bases=(models.Model,),
        ),
    ]
