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

     url(r'^password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password/reset/done/'},
        name="password_reset"),
    (r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : 'accounts/password/done/'}),
    (r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
)