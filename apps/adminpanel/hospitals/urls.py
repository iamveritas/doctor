from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.hospitals import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.HospitalsList.as_view()),
        name="list"),
    url(r"^page(?P<page>[0-9]+)/$", view=login_required(views.HospitalsList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddHospital.as_view()),
        name="add-hospital"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateHospital.as_view()),
        name="update-hospital"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteHospital.as_view()),
        name="delete-hospital"),

)