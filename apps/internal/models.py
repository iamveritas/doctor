# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):

    name = models.CharField(_("Область"), blank=False, max_length=20)

    def __unicode__(self):
        return unicode(self.name)


class City(models.Model):

    name = models.CharField(_("Місто"), blank=False, max_length=30)
    region = models.ForeignKey(Region,  verbose_name=_("Область"))

    def __unicode__(self):
        return unicode(self.name)


class Hospital(models.Model):

    name = models.CharField(_("Назва клініки"), blank=False, max_length=75)
    is_state = models.BooleanField(_("Державна"), default=True)
    type = models.CharField(_("Тип клініки"), blank=False, max_length=25)
    city = models.ForeignKey(City, verbose_name=_("Місто"))

    def __unicode__(self):
        return unicode(self.name)


class Speciality(models.Model):

    name = models.CharField(_("Спеціальність"), blank=False, max_length=30)

    def __unicode__(self):
        return unicode(self.name)


class Doctor(models.Model):

    first_name = models.CharField("Прізвище", blank=False, max_length=30)
    last_name = models.CharField(_("Ім'я"), blank=False, max_length=25)
    patronymic = models.CharField("По батькові", blank=False, max_length=30)
    speciality = models.ForeignKey(Speciality, verbose_name=_("Спеціальність"))
    hospitals = models.ManyToManyField(Hospital, blank=False, verbose_name=_("Клініка"))
    image = models.ImageField(_("Зображення"), upload_to="doctor_photos/",
                              null=True, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Efficiency(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Лікар"))

    def __unicode__(self):
        return unicode(self.doctor)


class Quality(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Лікар"))

    def __unicode__(self):
        return unicode(self.doctor)


class Respect(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Лікар"))

    def __unicode__(self):
        return unicode(self.doctor)


class Bribery(models.Model):
    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Лікар"))

    def __unicode__(self):
        return unicode(self.doctor)


class Comment(models.Model):

    content = models.TextField(_("Коментар"), blank=False, max_length=1000)
    plus = models.TextField(_("Позитивні якості"), blank=True, max_length=300)
    minus = models.TextField(_("Негативні якості"), blank=True, max_length=300)
    created = models.DateTimeField(_("Дата створення"), auto_now=False, auto_now_add=True)
    edited = models.DateTimeField(_("Дата редагування"), auto_now=True, auto_now_add=False)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Лікар"))

    def __unicode__(self):
        return unicode(self.doctor)


class Like(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    comment = models.ForeignKey(Comment, verbose_name=_("Коментар"))
    ip = models.IPAddressField("IP-адрес")
