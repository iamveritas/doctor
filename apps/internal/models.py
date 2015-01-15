# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField, get_thumbnail

from easy_thumbnails.fields import ThumbnailerImageField


SEX_CHOICES = (
    (None, "Оберіть стать"),
    ("M", "чоловіча"),
    ("F", "жіноча"),
)

STATUS_CHOICES = (
    ("False", "неактивний"),
    ("True", "активний"),
)


IS_STATE_CHOICES = (
    (None, "Обрати"),
    ("Y", "так"),
    ("N", "ні"),
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
    is_state = models.CharField("Державна", blank=False, max_length=1, choices=IS_STATE_CHOICES)
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
    sex = models.CharField("Стать", blank=False, max_length=1, choices=SEX_CHOICES)
    speciality = models.ForeignKey(Speciality, verbose_name="Спеціальність")
    user = models.ForeignKey(User, verbose_name="Хто створив")
    hospitals = models.ManyToManyField(Hospital, blank=False, verbose_name="Клініка")
    is_active = models.CharField("Статус", default=False, max_length=5, choices=STATUS_CHOICES)
    image = ThumbnailerImageField("Зображення", upload_to="doctor_photos/", blank=True,
                                  resize_source=dict(size=(128, 128), sharpen=True, autocrop=True, crop='smart'))
    #image = ImageField("Зображення", upload_to="doctor_photos/",
    #                          null=True, blank=True)
    recommend_yes = models.IntegerField("Рекомендують", blank=True, default=0)
    recommend_no = models.IntegerField("Не рекомендують", blank=True, default=0)
    created = models.DateTimeField("Дата створення", auto_now=False, auto_now_add=True)


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
    user = models.ForeignKey(User, verbose_name="Користувач")
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")
    is_active = models.CharField("Статус", default=False, max_length=5, choices=STATUS_CHOICES)
    created = models.DateTimeField("Дата створення", auto_now=False, auto_now_add=True)
    edited = models.DateTimeField("Дата редагування", auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

    def __unicode__(self):
        return unicode(self.content)


class CommentAnswer(models.Model):

    content = models.TextField("Коментар", blank=False, max_length=1000)
    comment = models.ForeignKey(Comment, verbose_name="Відгук")
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")
    is_active = models.CharField("Статус", default=True, max_length=5, choices=STATUS_CHOICES)
    created = models.DateTimeField("Дата створення", auto_now=False, auto_now_add=True)
    edited = models.DateTimeField("Дата редагування", auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

    def __unicode__(self):
        return unicode(self.content)


class Like(models.Model):

    rating = models.IntegerField("Рейтинг", blank=True)
    comment = models.ForeignKey(Comment, verbose_name="Коментар")
    ip = models.IPAddressField("IP-адрес")

    class Meta:
        verbose_name = "К-сть лайків"
        verbose_name_plural = "К-сть лайків"


class Recommendation(models.Model):

    user = models.ForeignKey(User, verbose_name="Користувач")
    doctor = models.ForeignKey(Doctor, verbose_name="Лікар")
    recommendation = models.NullBooleanField()

    class Meta:
        verbose_name = "Рекомендації пацієнтів"
        verbose_name_plural = "Рекомендації пацієнтів"

    def __unicode__(self):
        recommend = ''
        if self.recommendation == 1:
            recommend = ' recommended '
        elif self.recommendation == 0:
            recommend = ' not recommended '
        return unicode(self.user) + unicode(recommend) + unicode(self.doctor)

