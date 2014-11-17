from django.conf.urls import patterns, include, url
import settings

#from django.conf.urls import *

#from django.contrib.auth.decorators import login_required

from apps.accounts import views


urlpatterns = patterns("",
    url(r'^logout/$',views.logout),
    url(r'login/$',views.login),
    url(r"registration/$", views.registration,
        name="registration"),
)