# -*- coding: utf-8 -*-

from django.db import models


SEX_CHOICES = (
    ("0", "Оберіть стать"),
    ("1", "чоловіча"),
    ("2", "жіноча"),
)

IS_STATE_CHOICES = (
    ("0", "Обрати"),
    ("1", "так"),
    ("2", "ні"),
)


class Region(models.Model):

    name = models.CharField("Область", blank=False, max_length=20)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Області"

    def __unicode__(self):
        return unicode(self.name)


class City(models.Model):

    name = models.CharField("Місто", blank=False, max_length=30)
    region = models.ForeignKey(Region,  verbose_name="Область")

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"

    def __unicode__(self):
        return unicode(self.name)


class HospitalType(models.Model):

    name = models.CharField("Тип клініки", blank=False, max_length=25)

    class Meta:
        verbose_name = "Тип клініки"
        verbose_name_plural = "Тип клінік"

    def __unicode__(self):
        return unicode(self.name)


class Hospital(models.Model):

    name = models.CharField("Назва клініки", blank=False, max_length=75)
    is_state = models.CharField("Державна", default="", blank=False, max_length=1, choices=IS_STATE_CHOICES)
    type = models.ForeignKey(HospitalType, blank=False, verbose_name="Тип клініки")
    city = models.ForeignKey(City, verbose_name="Місто")
    address = models.CharField("Адреса (без назви міста)", blank=False, max_length=150)
    email = models.EmailField("Email", blank=True, max_length=50)
    phone = models.CharField("Телефон", blank=True, max_length=20)
    image = models.ImageField("Зображення", upload_to="doctor_photos/",
                              null=True, blank=True)

    class Meta:
        verbose_name = "Клініка"
        verbose_name_plural = "Клініки"

    def __unicode__(self):
        return unicode(self.name)


class Speciality(models.Model):

    name = models.CharField("Спеціальність", blank=False, max_length=30)

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __unicode__(self):
        return unicode(self.name)


class Doctor(models.Model):

    last_name = models.CharField("Прізвище", blank=False, max_length=30)
    first_name = models.CharField("Ім'я", blank=False, max_length=25)
    patronymic = models.CharField("По батькові", blank=False, max_length=30)
    sex = models.CharField("Стать", default="", blank=False, max_length=1, choices=SEX_CHOICES)
    speciality = models.ForeignKey(Speciality, verbose_name="Спеціальність")
    hospitals = models.ManyToManyField(Hospital, blank=False, verbose_name="Клініка")
    image = models.ImageField("Зображення", upload_to="doctor_photos/",
                              null=True, blank=True)

    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Efficiency(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    class Meta:
        verbose_name = "Ефективність"
        verbose_name_plural = "Ефективності"

    def __unicode__(self):
        return unicode(self.doctor)


class Quality(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    class Meta:
        verbose_name = "Якість"
        verbose_name_plural = "Якості"

    def __unicode__(self):
        return unicode(self.doctor)


class Respect(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    class Meta:
        verbose_name = "Відношення до людей"
        verbose_name_plural = "Відношення до людей"

    def __unicode__(self):
        return unicode(self.doctor)


class Bribery(models.Model):
    rating = models.IntegerField("Рейтинг", blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    class Meta:
        verbose_name = "Відношення до взяток"
        verbose_name_plural = "Відношення до взяток"

    def __unicode__(self):
        return unicode(self.doctor)


class Comment(models.Model):

    content = models.TextField("Коментар", blank=False, max_length=1000)
    plus = models.TextField("Позитивні якості", blank=True, max_length=300)
    minus = models.TextField("Негативні якості", blank=True, max_length=300)
    created = models.DateTimeField("Дата створення", auto_now=False, auto_now_add=True)
    edited = models.DateTimeField("Дата редагування", auto_now=True, auto_now_add=False)
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

    def __unicode__(self):
        return unicode(self.doctor)


class Like(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    comment = models.ForeignKey(Comment, verbose_name="Коментар")
    ip = models.IPAddressField("IP-адрес")

    class Meta:
        verbose_name = "К-сть лайків"
        verbose_name_plural = "К-сть лайків"