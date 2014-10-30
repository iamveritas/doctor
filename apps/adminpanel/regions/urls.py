from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.regions import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.RegionsList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddRegion.as_view()),
        name="add-region"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateRegion.as_view()),
        name="update-region"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteRegion.as_view()),
        name="delete-region"),

)