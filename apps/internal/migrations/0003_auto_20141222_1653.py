# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0002_doctor_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctoruser',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctoruser',
            name='user',
        ),
        migrations.DeleteModel(
            name='DoctorUser',
        ),
    ]
