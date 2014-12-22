from django.conf.urls import patterns, include, url
import settings

#from django.conf.urls import *

#from django.contrib.auth.decorators import login_required

from apps.accounts import views

from apps.accounts.views import LoginForm, UserDetail, UserDoctorCreate



urlpatterns = patterns("",
    url(r'login/$',LoginForm.as_view(), name="login"),
    url(r'(?P<pk>\d+)/$',UserDetail.as_view(), name="personal_page"),
    url(r'^doctor/$', UserDoctorCreate.as_view(), name="user_doctor"),

    url(r'^logout/$',views.logout, name="logout"),
#    url(r'login/$',views.login, name="login"),
    url(r"registration/$", views.registration, name="registration"),
)