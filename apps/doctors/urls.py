from django.conf.urls import patterns, include, url
import settings
from django.contrib.auth.decorators import login_required
#from apps.doctors import views

from apps.doctors.views import (DoctorList, DoctorDetail, DoctorCreate, HospitalCreate,
                                CommentCreate, CommentUpdate)

urlpatterns = patterns("",
    url(r'^$', DoctorList.as_view(), name="doctors"),
    url(r'^(?P<pk>\d+)/$', DoctorDetail.as_view(), name="doctor_profile"),
    url(r'^add/$', DoctorCreate.as_view(), name="add-doctor"),
    url(r'^newhospital/$', HospitalCreate.as_view(), name="add-hospital"),
    url(r'^(?P<pk>\d+)/newcomment/$', CommentCreate.as_view(), name="add-comment"),
    url(r'^comment/(?P<pk>\d+)/$', CommentUpdate.as_view(), name="edit-comment"),
    url(r'^(?P<pk>\d+)/(?P<recommend>[a-z]{2,3})/$', DoctorDetail.as_view()),
)