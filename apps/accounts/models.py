#-*-coding:utf8-*-
from django.db import models
from django.contrib.auth.models import User
from apps.internal.models import Doctor

SEX_CHOICES = (
    (None, "Оберіть стать"),
    ("M", "чоловіча"),
    ("F", "жіноча"),
)


class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True, related_name='profile')
    photo = models.TextField()
    sex = models.CharField("Стать", blank=False, max_length=1, choices=SEX_CHOICES)

    def __unicode__(self):
        return unicode(self.photo)


class UserDoctor(models.Model):
    user = models.OneToOneField(User)
    doctor = models.OneToOneField(Doctor, verbose_name="Лікар")
    status = models.BooleanField(default=False)

    def __unicode__(self):
        result = unicode(self.user)+u' ідентифікований як лікар '+unicode(self.doctor)
        return result

