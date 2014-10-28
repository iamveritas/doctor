from django.conf.urls import *
from django.contrib.auth.decorators import login_required

from apps.adminpanel.doctors import views

urlpatterns = patterns("",
    url(r"^$", view=login_required(views.DoctorList.as_view()),
        name="index"),

    #url(r"^developers/", include("apps.adminpanel.developers.urls",
    #                             namespace="developers")),

    #url(r"^customers/", include("apps.adminpanel.customers.urls",
    #                            namespace="customers")),

    #url(r"^projects/", include("apps.adminpanel.projects.urls",
    #                           namespace="projects")),

    #url(r"^reviews/", include("apps.adminpanel.reviews.urls",
    #                          namespace="reviews")),
)
