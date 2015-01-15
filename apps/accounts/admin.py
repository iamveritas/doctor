#-*-coding:utf8-*-
from django.contrib import admin
from apps.accounts.models import (UserDoctor, UserProfile, UserSetting)

admin.site.register(UserDoctor)
admin.site.register(UserProfile)
admin.site.register(UserSetting)
