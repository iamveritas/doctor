from django.conf.urls import patterns, include, url
import settings
from apps.accounts.views import (UserLogin, UserDetail, UserDoctorCreate, UserCreate,
                                 logout,)
#from django.contrib.auth.decorators import login_required


urlpatterns = patterns("",
    url(r'login/$',UserLogin.as_view(), name="login"),
    url(r'(?P<pk>\d+)/$',UserDetail.as_view(), name="personal_page"),
    url(r'^doctor/$', UserDoctorCreate.as_view(), name="user_doctor"),
    url(r"registration/$", UserCreate.as_view(), name="registration"),

    url(r'^logout/$',logout, name="logout"),
)