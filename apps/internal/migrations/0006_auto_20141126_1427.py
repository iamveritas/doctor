# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0005_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
