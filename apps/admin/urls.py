from django.conf.urls import *
from django.contrib.auth.decorators import login_required

#from apps.admin.developers import views

urlpatterns = patterns("",
    #url(r"^$", view=login_required(views.DevelopersList.as_view()),
    #    name="index"),

    #url(r"^developers/", include("apps.admin.developers.urls",
    #                             namespace="developers")),

    #url(r"^customers/", include("apps.admin.customers.urls",
    #                            namespace="customers")),

    #url(r"^projects/", include("apps.admin.projects.urls",
    #                           namespace="projects")),

    #url(r"^reviews/", include("apps.admin.reviews.urls",
    #                          namespace="reviews")),
)
