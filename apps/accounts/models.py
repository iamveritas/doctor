#-*-coding:utf8-*-
from django.db import models
from django.contrib.auth.models import User
from apps.internal.models import Doctor
from easy_thumbnails.fields import ThumbnailerImageField

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    photo = models.TextField()

    def __unicode__(self):
        return unicode(self.photo)


class UserSetting(models.Model):
    user = models.ForeignKey(User)
    last_name = models.CharField("Прізвище", blank=True, max_length=30)
    first_name = models.CharField("Ім'я", blank=True, max_length=25)
    photo = ThumbnailerImageField("Фотографія", blank=True, upload_to="user_photos/",
                              resize_source=dict(size=(128, 128), sharpen=True, autocrop=True, crop='smart'))

    def __unicode__(self):
        return unicode(self.photo)


class UserDoctor(models.Model):
    user = models.OneToOneField(User)
    doctor = models.OneToOneField(Doctor, verbose_name="Лікар", error_messages={'unique': 'З цим лікарем ідентифіковано іншого користувача. Якщо у Вас виникли питання, зверніться до адміністратора сайту.'})
    status = models.BooleanField(default=False)

    def __unicode__(self):
        result = unicode(self.user)+u' ідентифікований як лікар '+unicode(self.doctor)
        return result

