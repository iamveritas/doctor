from django.conf.urls import patterns, include, url
import settings

#from django.conf.urls import *

#from django.contrib.auth.decorators import login_required

from apps.accounts import views


urlpatterns = patterns("",
    url(r'^logout/$',views.logout, name="logout"),
    url(r'login/$',views.login, name="login"),
    url(r"registration/$", views.registration, name="registration"),
)