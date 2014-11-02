# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bribery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0456\u0434\u043d\u043e\u0448\u0435\u043d\u043d\u044f \u0434\u043e \u0432\u0437\u044f\u0442\u043e\u043a',
                'verbose_name_plural': '\u0412\u0456\u0434\u043d\u043e\u0448\u0435\u043d\u043d\u044f \u0434\u043e \u0432\u0437\u044f\u0442\u043e\u043a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x82\xd0\xbe')),
            ],
            options={
                'verbose_name': '\u041c\u0456\u0441\u0442\u043e',
                'verbose_name_plural': '\u041c\u0456\u0441\u0442\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=1000, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80')),
                ('plus', models.TextField(max_length=300, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb7\xd0\xb8\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x96 \xd1\x8f\xd0\xba\xd0\xbe\xd1\x81\xd1\x82\xd1\x96', blank=True)),
                ('minus', models.TextField(max_length=300, verbose_name=b'\xd0\x9d\xd0\xb5\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x96 \xd1\x8f\xd0\xba\xd0\xbe\xd1\x81\xd1\x82\xd1\x96', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd1\x82\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xb3\xd1\x83\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440',
                'verbose_name_plural': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5')),
                ('first_name', models.CharField(max_length=25, verbose_name=b"\xd0\x86\xd0\xbc'\xd1\x8f")),
                ('patronymic', models.CharField(max_length=30, verbose_name=b'\xd0\x9f\xd0\xbe \xd0\xb1\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96')),
                ('sex', models.CharField(max_length=1, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c', choices=[(None, b'\xd0\x9e\xd0\xb1\xd0\xb5\xd1\x80\xd1\x96\xd1\x82\xd1\x8c \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c'), (b'M', b'\xd1\x87\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd1\x96\xd1\x87\xd0\xb0'), (b'F', b'\xd0\xb6\xd1\x96\xd0\xbd\xd0\xbe\xd1\x87\xd0\xb0')])),
                ('image', models.ImageField(upload_to=b'doctor_photos/', null=True, verbose_name=b'\xd0\x97\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', blank=True)),
            ],
            options={
                'verbose_name': '\u041b\u0456\u043a\u0430\u0440',
                'verbose_name_plural': '\u041b\u0456\u043a\u0430\u0440\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Efficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3', blank=True)),
                ('doctor', models.ForeignKey(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', to='internal.Doctor')),
            ],
            options={
                'verbose_name': '\u0415\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c',
                'verbose_name_plural': '\u0415\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xba\xd0\xbb\xd1\x96\xd0\xbd\xd1\x96\xd0\xba\xd0\xb8')),
                ('is_state', models.CharField(max_length=1, verbose_name=b'\xd0\x94\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0', choices=[(None, b'\xd0\x9e\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd0\xb8'), (b'Y', b'\xd1\x82\xd0\xb0\xd0\xba'), (b'N', b'\xd0\xbd\xd1\x96')])),
                ('address', models.CharField(max_length=150, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81\xd0\xb0 (\xd0\xb1\xd0\xb5\xd0\xb7 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb8 \xd0\xbc\xd1\x96\xd1\x81\xd1\x82\xd0\xb0)')),
                ('email', models.EmailField(max_length=50, verbose_name=b'Email', blank=True)),
                ('phone', models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True)),
                ('image', models.ImageField(upload_to=b'doctor_photos/', null=True, verbose_name=b'\xd0\x97\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f', blank=True)),
                ('city', models.ForeignKey(verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x82\xd0\xbe', to='internal.City')),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0456\u043d\u0456\u043a\u0430',
                'verbose_name_plural': '\u041a\u043b\u0456\u043d\u0456\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HospitalType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xba\xd0\xbb\xd1\x96\xd0\xbd\xd1\x96\xd0\xba\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043a\u043b\u0456\u043d\u0456\u043a\u0438',
                'verbose_name_plural': '\u0422\u0438\u043f \u043a\u043b\u0456\u043d\u0456\u043a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3', blank=True)),
                ('ip', models.IPAddressField(verbose_name=b'IP-\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('comment', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80', to='internal.Comment')),
            ],
            options={
                'verbose_name': '\u041a-\u0441\u0442\u044c \u043b\u0430\u0439\u043a\u0456\u0432',
                'verbose_name_plural': '\u041a-\u0441\u0442\u044c \u043b\u0430\u0439\u043a\u0456\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3', blank=True)),
                ('doctor', models.ForeignKey(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', to='internal.Doctor')),
            ],
            options={
                'verbose_name': '\u042f\u043a\u0456\u0441\u0442\u044c',
                'verbose_name_plural': '\u042f\u043a\u043e\u0441\u0442\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u043b\u0430\u0441\u0442\u044c',
                'verbose_name_plural': '\u041e\u0431\u043b\u0430\u0441\u0442\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3', blank=True)),
                ('doctor', models.ForeignKey(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', to='internal.Doctor')),
            ],
            options={
                'verbose_name': '\u0412\u0456\u0434\u043d\u043e\u0448\u0435\u043d\u043d\u044f \u0434\u043e \u043b\u044e\u0434\u0435\u0439',
                'verbose_name_plural': '\u0412\u0456\u0434\u043d\u043e\u0448\u0435\u043d\u043d\u044f \u0434\u043e \u043b\u044e\u0434\u0435\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd1\x96\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x96\xd1\x81\xd1\x82\xd1\x8c')),
            ],
            options={
                'verbose_name': '\u0421\u043f\u0435\u0446\u0456\u0430\u043b\u044c\u043d\u0456\u0441\u0442\u044c',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0456\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hospital',
            name='type',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xba\xd0\xbb\xd1\x96\xd0\xbd\xd1\x96\xd0\xba\xd0\xb8', to='internal.HospitalType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospitals',
            field=models.ManyToManyField(to='internal.Hospital', verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x96\xd0\xbd\xd1\x96\xd0\xba\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd1\x96\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x96\xd1\x81\xd1\x82\xd1\x8c', to='internal.Speciality'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='doctor',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', to='internal.Doctor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(verbose_name=b'\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xb0\xd1\x81\xd1\x82\xd1\x8c', to='internal.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bribery',
            name='doctor',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd1\x96\xd0\xba\xd0\xb0\xd1\x80', to='internal.Doctor'),
            preserve_default=True,
        ),
    ]
