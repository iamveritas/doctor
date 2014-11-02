from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.specialities import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.SpecialitiesList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddSpeciality.as_view()),
        name="add-speciality"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateSpeciality.as_view()),
        name="update-speciality"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteSpeciality.as_view()),
        name="delete-speciality"),

)