from django.conf.urls import patterns, include, url
import settings
from django.contrib.auth.decorators import login_required
#from apps.doctors import views

from apps.doctors.views import (DoctorList, DoctorDetail, DoctorCreate, HospitalCreate,
                                CommentCreate, CommentUpdate, DoctorReviewList,
                                CommentAnswerCreate, CommentAnswerUpdate, ajax_test)

urlpatterns = patterns("",
    url(r'^$', DoctorList.as_view(), name="doctors"),
    url(r'^(?P<pk>\d+)/$', DoctorDetail.as_view(), name="doctor_profile"),
    url(r'^(?P<pk>\d+)/reviews/$', DoctorReviewList.as_view(), name="doctor_reviews"),
    url(r'^add/$', DoctorCreate.as_view(), name="add-doctor"),
    url(r'^newhospital/$', HospitalCreate.as_view(), name="add-hospital"),
    url(r'^(?P<pk>\d+)/newcomment/$', CommentCreate.as_view(), name="add-comment"),
    url(r'^comment/(?P<pk>\d+)/$', CommentUpdate.as_view(), name="edit-comment"),
    url(r'^comment/(?P<pk>\d+)/answer/$', CommentAnswerCreate.as_view(), name="answer-create"),
    url(r'^comment/answer/(?P<pk>\d+)$', CommentAnswerUpdate.as_view(), name="answer-update"),
    url(r'^(?P<pk>\d+)/(?P<recommend>[a-z]{2,3})/$', DoctorDetail.as_view()),
    url(r'^ajax_test/$', ajax_test),
)