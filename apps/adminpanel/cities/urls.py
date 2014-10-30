from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.cities import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.CitiesList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddCity.as_view()),
        name="add-city"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateCity.as_view()),
        name="update-city"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteCity.as_view()),
        name="delete-city"),

)