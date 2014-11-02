from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.doctors import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.DoctorsList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddDoctor.as_view()),
        name="add-doctor"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateDoctor.as_view()),
        name="update-doctor"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteDoctor.as_view()),
        name="delete-doctor"),
)