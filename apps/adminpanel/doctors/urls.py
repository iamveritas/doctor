from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.doctors import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.DoctorList.as_view()),
        name="list"),
)