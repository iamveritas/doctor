from django.conf.urls import patterns, include, url
import settings
from django.contrib.auth import views
from apps.accounts.views import (UserLogin, UserDetail, UserDoctorCreate, UserCreate,
                                 UserReviewList, logout, user_settings, user_settings_doctor)
#from django.contrib.auth.decorators import login_required


urlpatterns = patterns("",
    url(r'login/$',UserLogin.as_view(), name="login"),
    url(r'(?P<pk>\d+)/$',UserDetail.as_view(), name="personal_page"),
    url(r'(?P<pk>\d+)/reviews/$',UserReviewList.as_view(), name="user_reviews"),
    url(r'^doctor/$', UserDoctorCreate.as_view(), name="user_doctor"),
    url(r"registration/$", UserCreate.as_view(), name="registration"),

    url(r'^logout/$',logout, name="logout"),
    url(r'^settings/$',user_settings, name="user_settings"),
    url(r'^settingsdoc/$',user_settings_doctor, name="user_settings_doctor"),
)