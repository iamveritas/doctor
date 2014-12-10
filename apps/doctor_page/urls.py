from django.conf.urls import patterns, include, url
import settings
from django.contrib.auth.decorators import login_required
from apps.doctor_page import views


urlpatterns = patterns("",
    url(r'^$', views.doctors,
        name="doctors"),
    url(r'^newhospital/$', views.add_hospital,
        name="add-hospital"),
    url(r'^(?P<doctor_id>\d+)/(?P<recommend>[a-z]{2,3})/$', views.recommendation,
        name="doctor_profile"),
    url(r'^(?P<doctor_id>\d+)/newcomment/$', views.add_comment,
        name="add-comment"),
    url(r'^comment/(?P<comment_id>\d+)/$', views.edit_comment,
        name="edit-comment"),
    url(r'^(?P<doctor_id>\d{1})/$', views.doctor_profile,
        name="doctor_profile"),
    url(r'^add/$', views.add_doctor,
        name="add-doctor"),
    url(r'^doctor_user/$', views.doctor_user,
        name="doctor_user"),
)