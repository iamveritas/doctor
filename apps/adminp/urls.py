from django.conf.urls import *
from django.contrib.auth.decorators import login_required

from apps.adminp.doctors import views

urlpatterns = patterns("",
    url(r"^$", view=login_required(views.DoctorList.as_view()),
        name="index"),

    #url(r"^developers/", include("apps.adminp.developers.urls",
    #                             namespace="developers")),

    #url(r"^customers/", include("apps.adminp.customers.urls",
    #                            namespace="customers")),

    #url(r"^projects/", include("apps.adminp.projects.urls",
    #                           namespace="projects")),

    #url(r"^reviews/", include("apps.adminp.reviews.urls",
    #                          namespace="reviews")),
)
