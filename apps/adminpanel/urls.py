from django.conf.urls import *
from django.contrib.auth.decorators import login_required

from apps.adminpanel.doctors import views

urlpatterns = patterns("",
    url(r"^$", view=login_required(views.DoctorList.as_view()),
        name="index"),

    url(r"^doctors/", include("apps.adminpanel.doctors.urls",
                                 namespace="doctors")),

    url(r"^regions/", include("apps.adminpanel.regions.urls",
                                namespace="regions")),

    url(r"^cities/", include("apps.adminpanel.cities.urls",
                               namespace="cities")),

    url(r"^hospitals/", include("apps.adminpanel.hospitals.urls",
                              namespace="hospitals")),

    url(r"^specialities/", include("apps.adminpanel.specialities.urls",
                              namespace="specialities")),

    url(r"^doctor_reviews/", include("apps.adminpanel.doctor_reviews.urls",
                              namespace="doctor_reviews")),
)
