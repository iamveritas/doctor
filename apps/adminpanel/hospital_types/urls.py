from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.hospital_types import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.HospitalTypesList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddHospitalType.as_view()),
        name="add-hospital_types"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateHospitalType.as_view()),
        name="update-hospital_types"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteHospitalType.as_view()),
        name="delete-hospital_types"),

)
