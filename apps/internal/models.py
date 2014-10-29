# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):

    name = models.CharField("Область", blank=False, max_length=20)

    def __unicode__(self):
        return unicode(self.name)


class City(models.Model):

    name = models.CharField("Місто", blank=False, max_length=30)
    region = models.ForeignKey(Region,  verbose_name="Область")

    def __unicode__(self):
        return unicode(self.name)


class HospitalType(models.Model):

    name = models.CharField("Тип клініки", blank=False, max_length=25)
    
    def __unicode__(self):
        return unicode(self.name)


class Hospital(models.Model):

    name = models.CharField("Назва клініки", blank=False, max_length=75)
    is_state = models.BooleanField("Державна", default=True)
    type = models.ForeignKey(HospitalType, verbose_name="Тип клініки")
    city = models.ForeignKey(City, verbose_name="Місто")

    def __unicode__(self):
        return unicode(self.name)


class Speciality(models.Model):

    name = models.CharField("Спеціальність", blank=False, max_length=30)

    def __unicode__(self):
        return unicode(self.name)


class Doctor(models.Model):

    first_name = models.CharField("Прізвище", blank=False, max_length=30)
    last_name = models.CharField("Ім'я", blank=False, max_length=25)
    patronymic = models.CharField("По батькові", blank=False, max_length=30)
    speciality = models.ForeignKey(Speciality, verbose_name="Спеціальність")
    hospitals = models.ManyToManyField(Hospital, blank=False, verbose_name="Клініка")
    image = models.ImageField("Зображення", upload_to="doctor_photos/",
                              null=True, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Efficiency(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    def __unicode__(self):
        return unicode(self.doctor)


class Quality(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    def __unicode__(self):
        return unicode(self.doctor)


class Respect(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    def __unicode__(self):
        return unicode(self.doctor)


class Bribery(models.Model):
    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    def __unicode__(self):
        return unicode(self.doctor)


class Comment(models.Model):

    content = models.TextField("Коментар", blank=False, max_length=1000)
    plus = models.TextField("Позитивні якості", blank=True, max_length=300)
    minus = models.TextField("Негативні якості", blank=True, max_length=300)
    created = models.DateTimeField("Дата створення", auto_now=False, auto_now_add=True)
    edited = models.DateTimeField("Дата редагування", auto_now=True, auto_now_add=False)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    def __unicode__(self):
        return unicode(self.doctor)


class Like(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    comment = models.ForeignKey(Comment, verbose_name="Коментар")
    ip = models.IPAddressField("IP-адрес")
